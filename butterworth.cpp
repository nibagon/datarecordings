// inclide the fir library
#include "Fir1.h"
#include "Iir.h"
#include "clBP/include/clbp/Neuron.h"
#include "clBP/include/clbp/Layer.h"
#include "clBP/include/clbp/Net.h"
#include "parameters.h"
//#include <butterworth.h> not necessary 

#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
/*
#define NTAPS 100
#define LEARNING_RATE 0.05//fid a way of calculating this learning rate 
*/
int main (int,char**)
{
	int totalNINPUTS = NINPUTS;
	//initialise network
	int nNeurons[NLAYERS]={N1,N2,N3,N4,N5};//change this for th eno. of neurons
	int* nNeuronsp=nNeurons;
	Net* net = new Net(NLAYERS, nNeuronsp, totalNINPUTS);

	// define gains
	double errorGain = 1;
	double outputGain = 0.001; //0.005; changes

	//initialise the network
    net->initWeights(Neuron::W_RANDOM, Neuron::B_NONE);
    net->setLearningRate(LEARNINGRATE);

	/*
	Fir1 fir(NTAPS);
	fir.setLearningRate(LEARNING_RATE);*/
	
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
	hpemg.setup (samplingrate, cutoff_hemg);

	//buffer for the network inputs
	double inputsDelayed[totalNINPUTS];
	
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

		ecg_high=0.001 * hpecg.filter(ecg100);
		emg_high=0.001 * hpemg.filter(emg100);

		if (time > 2.5) {
		/*	
		double canceller = fir.filter(emg_high); 
		double output_signal = ecg_high - canceller;
		fir.lms_update(output_signal);*/
		
	    
		for (int i=totalNINPUTS; i>0; i--){
        	inputsDelayed[i]=inputsDelayed[i-1];
        }
		inputsDelayed[0]=emg_high;
		//propagate the inputs
        double* inputsDelayedPointer = &inputsDelayed[0];
        net->setInputs(inputsDelayedPointer);
        net->propInputs();
        //get the network's output
        double outPut = net->getOutput(0) * outputGain;
        //workout the error
        double leadError = (ecg_high - outPut) * errorGain;
        //propagate the error
        net->setError(leadError);
        net->propError();
        //do learning on the weights
        net->updateWeights();
        net->saveWeights();
        double weightDist = net->getWeightDistance();
												//0  ,1         ,2     ,3       ,4       ,5  ,6 
		fprintf(foutput,"%e %e %e %e %e %e %e\n",time,leadError,outPut,emg_high,ecg_high,ECG,EMG);
		}
		
	}
	fclose(finput);
    //fclose(noise);
	fclose(foutput);
	fprintf(stderr,"Written the filtered ECG to 'ecg_filtered.dat'\n");
	return 0;
}