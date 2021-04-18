// This is the only include you need
#include "Fir1.h"
#include "Iir.h"
#include <stdio.h>
const int numTrials = 2; //2//as in open and closed
Fir1 *outer_filter[numTrials];
//Fir1 *inner_filter[numTrials];

int main (int,char**)
{

/*
	Fir1 fir("coeff.dat");

	// resets the delay line to zero
	fir.reset ();
      
	// gets the number of taps
	int taps = fir.getTaps();

	printf("taps = %d\n",taps);
    const float samplingrate = 250; // Hz
    
	//Iir::RBJ::IIRNotch stop50;
	Iir::Butterworth::BandStop<6>stop50;
	double centerFrequency50=50; //change this one depending on where you are taking it
	double widthFrequency50=6;
	stop50.setup(samplingrate,centerFrequency50,widthFrequency50);
	//stop50.setup(samplingrate,centerFrequency50);

	Iir::Butterworth::BandStop<6>stop100;
	double centerFrequency100=100; //change this one depending on where you are taking it
	double widthFrequency100=6;
	stop100.setup(samplingrate,centerFrequency100,widthFrequency100);
	
	Iir::Butterworth::HighPass<2> hpecg;//maybe use the same
	const float cutoff_hecg = 1; // start cleaning from 0.5 remember fundamental frequency of ECG starts from 1hz
	hpecg.setup (samplingrate, cutoff_hecg);

	Iir::Butterworth::HighPass<2> hpemg;
	const float cutoff_hemg = 10; //EMG starts from 10 Hz
	hpemg.setup (samplingrate, cutoff_hemg);*/

	FILE *finput = fopen("data/lastrecordings/cleanECGaN.dat","rt");
	FILE *foutput = fopen("data/lastrecordings/cleanECGafir.dat","wt");
	for(int i=0;i<10000;i++) 
	{
        /*
		float t;
        float ecg;
        float emg;
		if (fscanf(finput,"%f\t%f\t%f\n",&t,&ecg,&emg)<1) break;
		//double b = fir.filter(ecg);
		//double c = fir.filter(emg);*/
        float ECG;
        float EMG;	
		float time;	
		if (fscanf(finput,"%e\t%e\t%e\n" ,&time,&ECG,&EMG)<1) break;
		//double ecg_high;
		double ecg50;
		double ecg100;
		//double emg_high;
		double emg50;
		double emg100;
/*
		ecg50=stop50.filter(ECG);
		emg50=stop50.filter(EMG);

		ecg100=stop100.filter(ecg50);
		emg100=stop100.filter(emg50);

		ecg_high=hpecg.filter(ecg100);//0.001
		emg_high=hpemg.filter(emg100);*/
        for (int i = 0; i < numTrials; i++) {
        outer_filter[i] = new Fir1("coeff.dat");
        outer_filter[i]->reset();
        }
        double ecg_high = outer_filter[0]->filter(ECG);
        double emg_high = outer_filter[1]->filter(EMG);
		fprintf(foutput,"%e\t%e\t%e\n",time,ecg_high,emg_high);
	}
	fclose(finput);
	fclose(foutput);
	fprintf(stderr,"Written the filtered ECG to 'ecg_filtered.dat'\n");
}