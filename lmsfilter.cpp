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
#define LEARNING_RATE 0.5//fid a way of calculating this learning rate 

int main (int,char**)
{
	// inits the filter
	Fir1 fir(NTAPS);
	fir.setLearningRate(LEARNING_RATE);

	FILE *finput = fopen("filtered_data2.dat","rt");

    FILE *foutput = fopen("clean_ecg.dat","wt");

	for(int i=0;;i++) 
	{
		float input_signal;
        float ref_noise;	
		float time;	
		if (fscanf(finput,"%e\t%e\t%e\n" ,&time,&input_signal,&ref_noise)<1) break;

		double canceller = fir.filter(ref_noise); //check 
		double output_signal = input_signal - canceller;
		fir.lms_update(output_signal);
		fprintf(foutput,"%e %e %e %e %e\n",time,output_signal,canceller,ref_noise,input_signal);
	}
	fclose(finput);
    //fclose(noise);
	fclose(foutput);
	fprintf(stderr,"Written the filtered ECG to 'clean_ecg.dat'\n");
}