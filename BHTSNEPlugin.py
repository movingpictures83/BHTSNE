import numpy
import bhtsne
import random
numpy.random.seed(1234)

class BHTSNEPlugin:
   def input(self, inputfile):
      self.data = numpy.genfromtxt(inputfile, delimiter=",")

   def run(self):
      self.result = bhtsne.tsne(self.data, rand_seed=1234)

   def output(self, outputfile):
      numpy.savetxt(outputfile, self.result, delimiter=",")      
