// LMS using fir1 library
// the idea is to remove EMG noise from ECG
// an input signal EMG is used in the fir filter, 
// tthis signal is then substracted from the recorded ECG

// inclide the fir library
#include "Fir1.h"
#include "Iir.h"
//#include <butterworth.h> not necessary 

#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define NTAPS 100
#define LEARNING_RATE 0.5//fid a way of calculating this learning rate 0.5 bicep

int main (int,char**)
{
	// inits the filter
	Fir1 fir(NTAPS);
	fir.setLearningRate(LEARNING_RATE);

	const float samplingrate = 250; // Hz

	//Iir::RBJ::IIRNotch stop50;
	Iir::Butterworth::BandStop<20>stop50;
	double centerFrequency50=50; //change this one depending on where you are taking it
	double widthFrequency50=4;
	int reqorder=4;
	stop50.setup(samplingrate,centerFrequency50,widthFrequency50);
	//stop50.setup(samplingrate,centerFrequency50,reqorder);

	Iir::Butterworth::BandStop<20>stop100;
	double centerFrequency100=100; //change this one depending on where you are taking it
	double widthFrequency100=4;
	stop100.setup(samplingrate,centerFrequency100,widthFrequency100);
	
	Iir::Butterworth::HighPass<2> hpecg;//maybe use the same
	const float cutoff_hecg = 0.5; // start cleaning from 0.5 remember fundamental frequency of ECG starts from 1hz
	hpecg.setup (samplingrate, cutoff_hecg);

	Iir::Butterworth::HighPass<2> hpemg;
	const float cutoff_hemg = 10; //EMG starts from 10 Hz
	hpemg.setup (samplingrate, cutoff_hemg);

	//FILE *finput = fopen("data/data2.21/bicep0.dat","rt");//the nice one
	FILE *finput = fopen("data/lastrecordings/WeightB_N.dat","rt");//the nice one
	//FILE *finput = fopen("data/data3.18/ECGarm2.dat","rt");
    FILE *foutput = fopen("2LMSfiltered_ecg.dat","wt");

	for(int i=0;;i++) 
	{
		float ECG;
        float EMG;	
		float time;	
		if (fscanf(finput,"%e\t%e\t%e\n" ,&time,&ECG,&EMG)<1) break;
		double ecg_high;
		double ecg50;
		double ecg100;
		double emg_high;
		double emg50;
		double emg100;
		/*
		float input_signal;
        float ref_noise;	
		float time;	
		if (fscanf(finput,"%e\t%e\t%e\n" ,&time,&input_signal,&ref_noise)<1) break;
		*/

		/*double canceller = fir.filter(ref_noise); //check 
		double output_signal = input_signal - canceller;
		fir.lms_update(output_signal);
		fprintf(foutput,"%e %e %e %e %e\n",time,output_signal,canceller,ref_noise,input_signal);
		*/
		ecg50=stop50.filter(ECG);
		emg50=stop50.filter(EMG);

		ecg100=stop100.filter(ecg50);
		emg100=stop100.filter(emg50);

		ecg_high=1000 * hpecg.filter(ecg100);//1000 -100
		emg_high=1000 * hpemg.filter(emg100);//1000 -100

		if (time > 2.5) {
		double canceller = fir.filter(emg_high); 
		double output_signal = ecg_high - canceller;
		fir.lms_update(output_signal);
												//0  ,1            ,2         ,3       ,4       ,5  ,6 
		fprintf(foutput,"%e %e %e %e %e %e %e\n",time,output_signal,canceller,ecg_high,emg_high,ECG,EMG);
		}
	}
	fclose(finput);
    //fclose(noise);
	fclose(foutput);
	fprintf(stderr,"Written the filtered ECG to 'LMSfiltered_ecg.dat'\n");
}