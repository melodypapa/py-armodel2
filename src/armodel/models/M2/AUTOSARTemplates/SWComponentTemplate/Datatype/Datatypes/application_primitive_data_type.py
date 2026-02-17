"""ApplicationPrimitiveDataType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 230)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 241)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1997)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 34)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_Datatypes.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_data_type import (
    ApplicationDataType,
)


class ApplicationPrimitiveDataType(ApplicationDataType):
    """AUTOSAR ApplicationPrimitiveDataType."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize ApplicationPrimitiveDataType."""
        super().__init__()


class ApplicationPrimitiveDataTypeBuilder:
    """Builder for ApplicationPrimitiveDataType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationPrimitiveDataType = ApplicationPrimitiveDataType()

    def build(self) -> ApplicationPrimitiveDataType:
        """Build and return ApplicationPrimitiveDataType object.

        Returns:
            ApplicationPrimitiveDataType instance
        """
        # TODO: Add validation
        return self._obj
