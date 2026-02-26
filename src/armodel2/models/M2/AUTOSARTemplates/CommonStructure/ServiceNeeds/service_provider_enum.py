"""AUTOSAR ServiceProviderEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 90)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

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

    ANY_STANDARDIZED = "ANY-STANDARDIZED"
    BASIC_SOFTWARE_MODE_MANAGER = "BASIC-SOFTWARE-MODE-MANAGER"
    COM_MANAGER = "COM-MANAGER"
    CRYPTO_KEY_MANAGEMENT = "CRYPTO-KEY-MANAGEMENT"
    CRYPTO_SERVICE_MANAGER = "CRYPTO-SERVICE-MANAGER"
    DEFAULT_ERROR_TRACER = "DEFAULT-ERROR-TRACER"
    DIAGNOSTIC_COMMUNICATION = "DIAGNOSTIC-COMMUNICATION"
    DIAGNOSTIC_EVENT_MANAGER = "DIAGNOSTIC-EVENT-MANAGER"
    DIAGNOSTIC_LOG_AND_TRACE = "DIAGNOSTIC-LOG-AND-TRACE"
    ECU_MANAGER = "ECU-MANAGER"
    ERROR_TRACER = "ERROR-TRACER"
    FUNCTION_INHIBITION_MANAGER = "FUNCTION-INHIBITION-MANAGER"
    HARDWARE_TEST_MANAGERINTRUSION_DETECTION = "HARDWARE-TEST-MANAGERINTRUSION-DETECTION"
    SECURITY = "SECURITY"
    J1939_DCM = "J1939-DCM"
    J1939_REQUEST_MANAGER = "J1939-REQUEST-MANAGER"
    SOFTWARE = "SOFTWARE"
    AUTOSAR = "A-U-T-O-S-A-R"
    NON_VOLATILE_RAM_MANAGER = "NON-VOLATILE-RAM-MANAGER"
    OPERATING_SYSTEM = "OPERATING-SYSTEM"
    SECURE_ON_BOARD_COMMUNICATION = "SECURE-ON-BOARD-COMMUNICATION"
    SYNC_BASE_TIME_MANAGER = "SYNC-BASE-TIME-MANAGER"
    V2X_FACILITIES = "V2X-FACILITIES"
    V2X_MANAGEMENT = "V2X-MANAGEMENT"
    VENDOR_SPECIFIC = "VENDOR-SPECIFIC"
    WATCH_DOG_MANAGER = "WATCH-DOG-MANAGER"
