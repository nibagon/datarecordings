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

	Iir::Butterworth::BandStop<2>stop;
	double centerFrequency=60; //change this one depending on where you are taking it
	double widthFrequency=6;
	stop.setup(samplingrate,centerFrequency,widthFrequency);

	Iir::Butterworth::LowPass<2> lp;//
	// filter parameters
	const float cutoff_low = 120; // Hz
	lp.setup (samplingrate, cutoff_low);

	Iir::Butterworth::HighPass<2> hpecg;//maybe use the same
	const float cutoff_hecg = 0.5; // start cleaning from 0.5 remember fundamental frequency of ECG starts from 1hz
	hpecg.setup (samplingrate, cutoff_hecg);

	Iir::Butterworth::HighPass<2> hpemg;
	const float cutoff_hemg = 50; // Hz
	hpemg.setup (samplingrate, cutoff_hemg);
	
	FILE *finput = fopen("unfiltered_data2.dat","rt");//where data is extracted
    FILE *foutput = fopen("ecg_filtered.dat","wt");//where data is saved

	for(int i=0;;i++) 
	{
		float ECG;
        float EMG;	
		float time;	
		if (fscanf(finput,"%e\t%e\t%e\n" ,&time,&ECG,&EMG)<1) break;

		ECG=stop.filter(ECG);
		EMG=stop.filter(EMG);

		double ecg_high;
		double ecg_low;
		double emg_high;
		double emg_low;

		ecg_low=lp.filter(ECG);
		emg_low=lp.filter(EMG);

		ecg_high=hpecg.filter(ecg_low);
		emg_high=hpemg.filter(emg_low);

		if (time > 2) {
		double canceller = fir.filter(emg_high); //check 
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