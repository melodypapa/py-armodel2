"""ServiceProviderEnum enumeration."""

from enum import Enum


class ServiceProviderEnum(Enum):
    """AUTOSAR ServiceProviderEnum enumeration."""

    ANYSTANDARDIZED = "anyStandardized"
    BASICSOFTWAREMODEMANAGER = "basicSoftwareModeManager"
    COMMANAGER = "comManager"
    CRYPTOKEYMANAGEMENT = "cryptoKeyManagement"
    CRYPTOSERVICEMANAGER = "cryptoServiceManager"
    DEFAULTERRORTRACER = "defaultErrorTracer"
    DIAGNOSTICCOMMUNICATION = "diagnosticCommunication"
    DIAGNOSTICEVENTMANAGER = "diagnosticEventManager"
    DIAGNOSTICLOGANDTRACE = "diagnosticLogAndTrace"
    ECUMANAGER = "ecuManager"
    ERRORTRACER = "errorTracer"
    FUNCTIONINHIBITIONMANAGER = "functionInhibitionManager"
    HARDWARETESTMANAGERINTRUSIONDETECTION = "hardwareTestManagerintrusionDetection"
    SECURITY = "Security"
    J1939DCM = "j1939Dcm"
    J1939REQUESTMANAGER = "j1939RequestManager"
    SOFTWARE = "Software"
    AUTOSAR = "AUTOSAR"
    NONVOLATILERAMMANAGER = "nonVolatileRamManager"
    OPERATINGSYSTEM = "operatingSystem"
    SECUREONBOARDCOMMUNICATION = "secureOnBoardCommunication"
    SYNCBASETIMEMANAGER = "syncBaseTimeManager"
    V2XFACILITIES = "v2xFacilities"
    V2XMANAGEMENT = "v2xManagement"
    VENDORSPECIFIC = "vendorSpecific"
    WATCHDOGMANAGER = "watchDogManager"
