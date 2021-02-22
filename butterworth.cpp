// inclide the fir library
#include "Fir1.h"
#include "Iir.h"
//#include <butterworth.h> not necessary 

#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define NTAPS 100
#define LEARNING_RATE 0.05//fid a way of calculating this learning rate 

int main (int,char**)
{
	// Declared all the filters that will be used 

	Fir1 fir(NTAPS);
	fir.setLearningRate(LEARNING_RATE);
	const float samplingrate = 250; // Hz

    /*const float mains = 50;
	Iir::RBJ::IIRNotch iirnotch;
	iirnotch.setup(samplingrate,mains);//48-52 instead of notch*/

	Iir::Butterworth::BandStop<2>stop50;
	double centerFrequency50=50; //change this one depending on where you are taking it
	double widthFrequency50=6;
	stop50.setup(samplingrate,centerFrequency50,widthFrequency50);

	Iir::Butterworth::BandStop<2>stop100;
	double centerFrequency100=100; //change this one depending on where you are taking it
	double widthFrequency100=6;
	stop100.setup(samplingrate,centerFrequency100,widthFrequency100);
	
	/*
	Iir::Butterworth::LowPass<2> lp;//
	const float cutoff_low = 120; // Hz
	lp.setup (samplingrate, cutoff_low);*/

	Iir::Butterworth::HighPass<2> hpecg;//maybe use the same
	const float cutoff_hecg = 1; // start cleaning from 0.5 remember fundamental frequency of ECG starts from 1hz
	hpecg.setup (samplingrate, cutoff_hecg);

	Iir::Butterworth::HighPass<2> hpemg;
	const float cutoff_hemg = 10; //EMG starts from 10 Hz
	hpemg.setup (samplingrate, cutoff_hemg);
	
	FILE *finput = fopen("data/data2.21/bicep0.dat","rt");//where data is extracted
    FILE *foutput = fopen("ecg_filtered.dat","wt");//where data is saved

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

		ecg50=stop50.filter(ECG);
		emg50=stop50.filter(EMG);

		ecg100=stop100.filter(ecg50);
		emg100=stop100.filter(emg50);
		/*
		ecg_low=lp.filter(ECG);
		emg_low=lp.filter(EMG);*/

		ecg_high=hpecg.filter(ECG);
		emg_high=hpemg.filter(EMG);

		if (time > 2) {
		double canceller = fir.filter(emg_high); 
		double output_signal = ecg_high - canceller;
		fir.lms_update(output_signal);
		fprintf(foutput,"%e %e %e %e %e %e\n",time,output_signal,canceller,emg_high,ecg_high,ECG);
		}
		
	}
	fclose(finput);
    //fclose(noise);
	fclose(foutput);
	fprintf(stderr,"Written the filtered ECG to 'ecg_filtered.dat'\n");
	return 0;
}