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
#define LEARNING_RATE 500//fid a way of calculating this learning rate 

int main (int,char**)
{
	// inits the filter
	Fir1 fir(NTAPS);
	fir.setLearningRate(LEARNING_RATE);
    // add 2 instances of iir filter before 
    //iir1 f1(sjsj)
    //nois = f1(noise)
    //read data from
	FILE *finput = fopen("01_164ecg_noise.dat","rt");
    FILE *noise = fopen("01_164just_noise.dat","rt");
	//FILE *finput = fopen("ecg50hz.dat","rt");

    //open file to write filtered data
    FILE *foutput = fopen("01164ecg_filtered.dat","wt");

	for(int i=0;;i++) 
	{
		double input_signal;
        double ref_noise;		
		if (fscanf(finput,"%le\n",&input_signal)<1) break; //fscanf(finput,"%e\t%e\t%e\n",&s1,s2,s3)  fscanf("%e\t%e\t%e... 
    	if (fscanf(noise,"%le\n",&ref_noise)<1) break;

        // finput and noise go directly to fir, add 2 instances of iir filter before 
		//double ref_noise = sin(2*M_PI/20*i);


		double canceller = fir.filter(ref_noise); //check 
		double output_signal = input_signal - canceller;
		fir.lms_update(output_signal);
		fprintf(foutput,"%e %e %e\n",output_signal,canceller,ref_noise);
	}
	fclose(finput);
    fclose(noise);
	fclose(foutput);
	fprintf(stderr,"Written the filtered ECG to 'ecg_filtered.dat'\n");
}
/*
int main (int,char**)
{
	// inits the filter
	Fir1 fir(NTAPS);
	fir.setLearningRate(LEARNING_RATE);

	FILE *finput = fopen("ecg50hz.dat","rt");
	FILE *foutput = fopen("ecg_filtered.dat","wt");
	for(int i=0;;i++) 
	{
		double input_signal;		
		if (fscanf(finput,"%lf\n",&input_signal)<1) break;
		double ref_noise = sin(2*M_PI/20*i);
		double canceller = fir.filter(ref_noise);
		double output_signal = input_signal - canceller;
		fir.lms_update(output_signal);
		fprintf(foutput,"%f %f %f\n",output_signal,canceller,ref_noise);
	}
	fclose(finput);
	fclose(foutput);
	fprintf(stderr,"Written the filtered ECG to 'ecg_filtered.dat'\n");
}
*/