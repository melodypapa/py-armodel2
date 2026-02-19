"""ApplicationPrimitiveDataType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 230)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 241)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1997)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 34)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_Datatypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_data_type import (
    ApplicationDataType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class ApplicationPrimitiveDataType(ApplicationDataType):
    """AUTOSAR ApplicationPrimitiveDataType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize ApplicationPrimitiveDataType."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationPrimitiveDataType":
        """Deserialize XML element to ApplicationPrimitiveDataType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationPrimitiveDataType object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        return obj



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
