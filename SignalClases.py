import scipy.io  

class OrgSignal:
        
    def __init__(self,srate) :
       
        self.srate = 10000 
    
    def getData(Foldnum, Filenum):  
        orgSignalDict = {
        'path' : 'Base de datos proyecto sin repeticion',
        'Folder' :['experimental CBX proyecto','experimental NaCl proyecto','experimental QUININA proyecto','experimental TMA proyecto' ],    
        'CBX' : ['FR-77_CBX_n', 'FR-78_CBX_n' , 'FR-80_CBX_n', 'FR-84_CBX_n', 'FR-90_CBX_n', 'FR-94_CBX_n', 'FR-95_CBX_n', 'FR-C_CBX_n'] ,
        'NaCl': ['R-45_NaCl_n', 'FR-83_NaCl_n','FR-89_NaCl_n','FR-91_NaCl_n'] ,
        'QUININA':['FR-77_QUININA_n', 'FR-78_QUININA_n', 'FR-79_QUININA_n', 'FR-80_QUININA_n', 'FR-84_QUININA_n', 'FR-90_QUININA_n', 'FR-94_QUININA_n', 'FR-95_QUININA_n'] ,
        'TMA':['FR-35_TMA_n', 'FR-83_TMA_n', 'FR-89_TMA_n', 'FR-91_TMA_n', 'R-25_TMA_n', 'R-26_TMA_n', 'R-45_TMA_n', 'R-50_TMA_n'],
        'labels' : ['HAD1','HADP2','HAD3','HADp4','HPD5','HPDp6','HPD7','HPDp8']    
        }
        
        orgFold = list(orgSignalDict.keys())   # Lista con nombres de llaves de diccionario original
        # print(orgFold)
        foldOS = orgSignalDict[orgFold[1]]     # Lista de nombres de folders principales
        # print(foldOS)
        orgFiles = orgSignalDict[orgFold[Foldnum + 2]]   # Lista con nombres de archivos por carpeta 
        # print(orgFiles)
        path = orgSignalDict[orgFold [0]]
        # print(path)
        
        orgPath = 'S:'+ '\\'+ '\\' + 'Proyecto Epilepsia' + '\\'+ '\\'+ path + '\\'+ '\\' + foldOS[Foldnum] + '\\'+ '\\' + orgFiles[Filenum] + '.mat'
        print(orgPath)

        orgSig = scipy.io.loadmat(orgPath) 
        orgSigData = orgSig['data']
        orgSigData = orgSigData.transpose()       
        return orgSigData,orgPath, orgFiles[Filenum]
    

class FiltSignal:
        
    def __init__(self,srate) :
        self.srate = 10000
        
    
    def getData(Foldnum, Filenum):
        
        filterSignalDict = {
        'path' : 'Base de datos filtrada',
        'Folder' :['CBX_f','NaCl_f','QUININA_f','TMA_f'],
        'CBX' : ['FR-77_CBX_f', 'FR-78_CBX_f' , 'FR-80_CBX_f', 'FR-84_CBX_f', 'FR-90_CBX_f', 'FR-94_CBX_f', 'FR-95_CBX_f', 'FR-C_CBX_f'] ,      
        'NaCl': ['R-45_NaCl_f', 'FR-83_NaCl_f' ,'FR-89_NaCl_f', 'FR-91_NaCl_f'] ,
        'QUININA':['FR-77_QUININA_f', 'FR-78_QUININA_f', 'FR-79_QUININA_f', 'FR-80_QUININA_f', 'FR-84_QUININA_f', 'FR-90_QUININA_f', 'FR-94_QUININA_f', 'FR-95_QUININA_f'] ,
        'TMA':['FR-35_TMA_f', 'FR-83_TMA_f', 'FR-89_TMA_f', 'FR-91_TMA_f', 'R-25_TMA_f', 'R-26_TMA_f', 'R-45_TMA_f', 'R-50_TMA_f'],
        'labels' : ['HAD1','HADP2','HAD3','HADp4','HPD5','HPDp6','HPD7','HPDp8']       
        }
                
        filtFold = list(filterSignalDict.keys())   # Lista con nombres de llaves de diccionario original
        # print(filtFold)
        foldFilt = filterSignalDict[filtFold[1]]     # Lista de nombres de folders principales
        # print(foldFilt)
        filtFiles = filterSignalDict[filtFold[Foldnum + 2]]   # Lista con nombres de los archivos en carpeta
        # print(filtFiles)
        pathFilt = filterSignalDict[filtFold[0]]
        # print(pathFilt)

        filtPaht = 'S:'+ '\\'+ '\\' + 'Proyecto Epilepsia' + '\\'+ '\\'+ pathFilt + '\\'+ '\\' + foldFilt[Foldnum] + '\\'+ '\\' + filtFiles[Filenum] + '\\'+ '\\' + filtFiles[Filenum] +'.mat'
        print(filtPaht)

        filtSig = scipy.io.loadmat(filtPaht) 
        filtSigData = filtSig['FilSignal'] 
        return filtSigData, filtPaht
    
    
class SWSignal:
    def __init__(self,srate) :
        self.srate = 10000
        
    
    def getData(Foldnum, Filenum):
        slowWaveDict = {
            'path' : 'Slow Wave Filter',
            'Folder' :['experimental CBX proyecto','experimental NaCl proyecto','experimental QUININA proyecto','experimental TMA proyecto'],   
            'CBX' : ['FR-77_CBX_SWF', 'FR-78_CBX_SWF' , 'FR-80_CBX_SWF', 'FR-84_CBX_SWF', 'FR-90_CBX_SWF', 'FR-94_CBX_SWF', 'FR-95_CBX_SWF', 'FR-C_CBX_SWF'], 
            'NaCl': ['R-45_NaCl_SWF', 'FR-83_NaCl_SWF','FR-89_NaCl_SWF','FR-91_NaCl_SWF'] ,
            'QUININA':['FR-77_QUININA_SWF', 'FR-78_QUININA_SWF', 'FR-79_QUININA_SWF', 'FR-80_QUININA_SWF', 'FR-84_QUININA_SWF', 'FR-90_QUININA_SWF', 'FR-94_QUININA_SWF', 'FR-95_QUININA_SWF'] ,
            'TMA':['FR-35_TMA_SWF', 'FR-83_TMA_SWF', 'FR-89_TMA_SWF', 'FR-91_TMA_SWF', 'R-25_TMA_SWF', 'R-26_TMA_SWF', 'R-45_TMA_SWF', 'R-50_TMA_SWF'],
            'labels' : ['HAD1','HADP2','HAD3','HADp4','HPD5','HPDp6','HPD7','HPDp8']
        }
                
        SWFold = list(slowWaveDict.keys())   # Lista con nombres de llaves de diccionario original
        # print(SWFold)
        foldSW = slowWaveDict[SWFold[1]]     # Lista de nombres de folders principales
        # print(foldSW)
        SWFiles = slowWaveDict[SWFold[Foldnum + 2]]   # Lista con nombres de archivos en carpeta [n+1]
        # print(SWFiles)
        pathSW = slowWaveDict[SWFold[0]]
        # print(pathSW)

        SWPaht = 'S:'+ '\\'+ '\\' + 'Proyecto Epilepsia' + '\\'+ '\\' + pathSW + '\\'+ '\\' + foldSW[Foldnum] + '\\'+ '\\' + SWFiles[Filenum] + '\\'+ '\\' + SWFiles[Filenum] +'.mat'
        print(SWPaht)

        SWSig = scipy.io.loadmat(SWPaht) 
        SWSigData = SWSig['FiltSignal']
        SWSigData = SWSigData.transpose()

        return SWSigData 
    
class IndSW:
    def __init__(self,srate) :
        self.srate = 10000        
    
    def getData(Foldnum, Filenum,lb):
        indSWDict = {
            'path' : 'Slow Wave Index',
            'Folder' :['experimental CBX proyecto','experimental NaCl proyecto','experimental QUININA proyecto','experimental TMA proyecto'],    
            'CBX' : ['FR-77_CBX_ind', 'FR-78_CBX_ind' ,'FR-80_CBX_ind', 'FR-84_CBX_ind', 'FR-90_CBX_ind', 'FR-94_CBX_ind', 'FR-95_CBX_ind', 'FR-C_CBX_ind'] ,
            'NaCl': ['R-45_NaCl_ind', 'FR-83_NaCl_ind','FR-89_NaCl_ind','FR-91_NaCl_ind'] ,
            'QUININA':['FR-77_QUININA_ind', 'FR-78_QUININA_ind', 'FR-79_QUININA_ind', 'FR-80_QUININA_ind', 'FR-84_QUININA_ind', 'FR-90_QUININA_ind', 'FR-94_QUININA_ind', 'FR-95_QUININA_ind'] ,
            'TMA':['FR-35_TMA_ind', 'FR-83_TMA_ind', 'FR-89_TMA_ind', 'FR-91_TMA_ind', 'R-25_TMA_ind', 'R-26_TMA_ind', 'R-45_TMA_ind', 'R-50_TMA_ind'],
            'labels' : ['HAD1','HADP2','HAD3','HADp4','HPD5','HPDp6','HPD7','HPDp8']
        }
                
        IndFold = list(indSWDict.keys())   # Lista con nombres de llaves de diccionario original
        # print(IndFold)
        IndFilt = indSWDict[IndFold[1]]     # Lista de nombres de folders principales
        # print(IndFilt)
        IndFiles = indSWDict[IndFold[Foldnum + 2]]   # Lista con nombres de los archivos en carpeta
        # print(IndFiles)
        pathInd = indSWDict[IndFold[0]]
        # print(pathInd)
        label = indSWDict[IndFold[6]]
        # print(label)

        IndPaht = 'S:'+ '\\'+ '\\' + 'Proyecto Epilepsia' + '\\'+ '\\'+ pathInd + '\\'+ '\\' + IndFilt[Foldnum] + '\\'+ '\\' + IndFiles[Filenum] + '\\'+ '\\' + label[lb]+'\\'+ '\\' + IndFiles[Filenum] +'_'+ label[lb]+'.mat'
        print(IndPaht)

        IndSig = scipy.io.loadmat(IndPaht) 
        IndSigData = IndSig['SlowWave']
        # print(IndSigData.shape)
        
        return IndSigData, label[lb]

class saveData:
    def getData(Foldnum, Filenum, lb):
        indDF = {
            'path' : 'DataFrames',
            'Folder' :['experimental CBX proyecto','experimental NaCl proyecto','experimental QUININA proyecto','experimental TMA proyecto'],
            'CBX' : ['FR-77_CBX', 'FR-78_CBX' , 'FR-80_CBX', 'FR-84_CBX', 'FR-90_CBX', 'FR-94_CBX', 'FR-95_CBX', 'FR-C_CBX'] ,    
            'NaCl': ['R-45_NaCl', 'FR-83_NaCl','FR-89_NaCl','FR-91_NaCl'] ,
            'QUININA':['FR-77_QUININA', 'FR-78_QUININA', 'FR-79_QUININA', 'FR-80_QUININA', 'FR-84_QUININA', 'FR-90_QUININA', 'FR-94_QUININA', 'FR-95_QUININA'] ,
            'TMA':['FR-35_TMA', 'FR-83_TMA', 'FR-89_TMA', 'FR-91_TMA', 'R-25_TMA', 'R-26_TMA', 'R-45_TMA', 'R-50_TMA'],
            'labels' : ['HAD1','HADP2','HAD3','HADp4','HPD5','HPDp6','HPD7','HPDp8']
        }
                
        IndFold = list(indDF.keys())   # Lista con nombres de llaves de diccionario original
        # print(IndFold)
        IndFilt = indDF[IndFold[1]]     # Lista de nombres de folders principales
        # print(IndFilt)
        IndFiles = indDF[IndFold[Foldnum + 2]]   # Lista con nombres de los archivos en carpeta
        # print(IndFiles)
        pathInd = indDF[IndFold[0]]
        # print(pathInd)
        label = indDF[IndFold[6]]
        # print(label)

        savePath = 'S:'+ '\\'+ '\\' + 'Proyecto Epilepsia' + '\\'+ '\\'+ pathInd + '\\'+ '\\' + IndFilt[Foldnum] + '\\'+ '\\' + IndFiles[Filenum] +'\\'+ '\\'+ label[lb] +'\\' + IndFiles[Filenum] + '_' + label[lb]  +'.csv'
        print(savePath)
        
        return savePath
    
class saveDataSR:
    def getData(Foldnum, Filenum, lb):
        indDF = {
            'path' : 'DataFrames SR',
            'Folder' :['experimental CBX proyecto','experimental NaCl proyecto','experimental QUININA proyecto','experimental TMA proyecto'],
            'CBX' : ['FR-77_CBX', 'FR-78_CBX' , 'FR-80_CBX', 'FR-84_CBX', 'FR-90_CBX', 'FR-94_CBX', 'FR-95_CBX', 'FR-C_CBX'] ,    
            'NaCl': ['R-45_NaCl', 'FR-83_NaCl','FR-89_NaCl','FR-91_NaCl'] ,
            'QUININA':['FR-77_QUININA', 'FR-78_QUININA', 'FR-79_QUININA', 'FR-80_QUININA', 'FR-84_QUININA', 'FR-90_QUININA', 'FR-94_QUININA', 'FR-95_QUININA'] ,
            'TMA':['FR-35_TMA', 'FR-83_TMA', 'FR-89_TMA', 'FR-91_TMA', 'R-25_TMA', 'R-26_TMA', 'R-45_TMA', 'R-50_TMA'],
            'labels' : ['HAD1','HADP2','HAD3','HADp4','HPD5','HPDp6','HPD7','HPDp8']
        }
                
        IndFold = list(indDF.keys())   # Lista con nombres de llaves de diccionario original
        # print(IndFold)
        IndFilt = indDF[IndFold[1]]     # Lista de nombres de folders principales
        # print(IndFilt)
        IndFiles = indDF[IndFold[Foldnum + 2]]   # Lista con nombres de los archivos en carpeta
        # print(IndFiles)
        pathInd = indDF[IndFold[0]]
        # print(pathInd)
        label = indDF[IndFold[6]]
        # print(label)

        savePath = 'S:'+ '\\'+ '\\' + 'Proyecto Epilepsia' + '\\'+ '\\'+ pathInd + '\\'+ '\\' + IndFilt[Foldnum] + '\\'+ '\\' + IndFiles[Filenum] +'\\'+ '\\'+ label[lb] +'\\' + IndFiles[Filenum] + '_' + label[lb] + '_SR' + '.csv'
        print(savePath)
        
        return savePath

    
class saveWV:
    def getData(Foldnum, Filenum, lb, ind, inPnt, fnPnt):
        indDF = {
            'path' : 'Wavelet Images',
            'Folder' :['experimental CBX proyecto','experimental NaCl proyecto','experimental QUININA proyecto','experimental TMA proyecto'],    
            'CBX' : ['FR-77_CBX', 'FR-78_CBX' , 'FR-80_CBX', 'FR-84_CBX', 'FR-90_CBX', 'FR-94_CBX', 'FR-95_CBX', 'FR-C_CBX'] ,
            'NaCl': ['R-45_NaCl', 'FR-83_NaCl','FR-89_NaCl','FR-91_NaCl'] ,
            'QUININA':['FR-77_QUININA', 'FR-78_QUININA', 'FR-79_QUININA', 'FR-80_QUININA', 'FR-84_QUININA', 'FR-90_QUININA', 'FR-94_QUININA', 'FR-95_QUININA'] ,
            'TMA':['FR-35_TMA', 'FR-83_TMA', 'FR-89_TMA', 'FR-91_TMA', 'R-25_TMA', 'R-26_TMA', 'R-45_TMA', 'R-50_TMA'],
            'labels' : ['HAD1','HADP2','HAD3','HADp4','HPD5','HPDp6','HPD7','HPDp8']
        }
                
        IndFold = list(indDF.keys())   # Lista con nombres de llaves de diccionario original
        # print(IndFold)
        IndFilt = indDF[IndFold[1]]     # Lista de nombres de folders principales
        # print(IndFilt)
        IndFiles = indDF[IndFold[Foldnum + 2]]   # Lista con nombres de los archivos en carpeta
        # print(IndFiles)
        pathInd = indDF[IndFold[0]]
        # print(pathInd)
        label = indDF[IndFold[6]]
        # print(label)

        readPath = 'S:'+ '\\'+ '\\' + 'Proyecto Epilepsia' + '\\'+ '\\'+ pathInd + '\\'+ '\\' + IndFilt[Foldnum] + '\\'+ '\\' + IndFiles[Filenum] +'\\'+ '\\'+ label[lb] +'\\' + IndFiles[Filenum] + '_' + label[lb] +'-'+ inPnt+'-'+fnPnt+'.png'
        print(readPath)
        
        return readPath
