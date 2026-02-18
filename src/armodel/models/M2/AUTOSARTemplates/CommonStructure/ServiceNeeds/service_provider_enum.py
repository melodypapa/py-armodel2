"""AUTOSAR ServiceProviderEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 90)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class ServiceProviderEnum(AREnum):
    """AUTOSAR ServiceProviderEnum enumeration.

    This enum inherits from AREnum, which provides:
    - serialize(): XML serialization
    - deserialize(): XML deserialization with automatic member matching
    - Transparent equality comparison with string values
    """

    def __init__(self, value: str) -> None:
        """Initialize enum member.

        Args:
            value: The enum value as a string
        """
        self._value_ = value

    ANY_STANDARDIZED = "anyStandardized"
    BASIC_SOFTWARE_MODE_MANAGER = "basicSoftwareModeManager"
    COM_MANAGER = "comManager"
    CRYPTO_KEY_MANAGEMENT = "cryptoKeyManagement"
    CRYPTO_SERVICE_MANAGER = "cryptoServiceManager"
    DEFAULT_ERROR_TRACER = "defaultErrorTracer"
    DIAGNOSTIC_COMMUNICATION = "diagnosticCommunication"
    DIAGNOSTIC_EVENT_MANAGER = "diagnosticEventManager"
    DIAGNOSTIC_LOG_AND_TRACE = "diagnosticLogAndTrace"
    ECU_MANAGER = "ecuManager"
    ERROR_TRACER = "errorTracer"
    FUNCTION_INHIBITION_MANAGER = "functionInhibitionManager"
    HARDWARE_TEST_MANAGERINTRUSION_DETECTION = "hardwareTestManagerintrusionDetection"
    SECURITY = "Security"
    J1939_DCM = "j1939Dcm"
    J1939_REQUEST_MANAGER = "j1939RequestManager"
    SOFTWARE = "Software"
    AUTOSAR = "AUTOSAR"
    NON_VOLATILE_RAM_MANAGER = "nonVolatileRamManager"
    OPERATING_SYSTEM = "operatingSystem"
    SECURE_ON_BOARD_COMMUNICATION = "secureOnBoardCommunication"
    SYNC_BASE_TIME_MANAGER = "syncBaseTimeManager"
    V2X_FACILITIES = "v2xFacilities"
    V2X_MANAGEMENT = "v2xManagement"
    VENDOR_SPECIFIC = "vendorSpecific"
    WATCH_DOG_MANAGER = "watchDogManager"
