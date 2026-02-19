"""ApplicationRecordDataType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 261)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1997)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 34)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_Datatypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_composite_data_type import (
    ApplicationCompositeDataType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class ApplicationRecordDataType(ApplicationCompositeDataType):
    """AUTOSAR ApplicationRecordDataType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    elements: list[Any]
    def __init__(self) -> None:
        """Initialize ApplicationRecordDataType."""
        super().__init__()
        self.elements: list[Any] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationRecordDataType":
        """Deserialize XML element to ApplicationRecordDataType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationRecordDataType object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse elements (list)
        obj.elements = []
        for child in ARObject._find_all_child_elements(element, "ELEMENTS"):
            elements_value = child.text
            obj.elements.append(elements_value)

        return obj



class ApplicationRecordDataTypeBuilder:
    """Builder for ApplicationRecordDataType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationRecordDataType = ApplicationRecordDataType()

    def build(self) -> ApplicationRecordDataType:
        """Build and return ApplicationRecordDataType object.

        Returns:
            ApplicationRecordDataType instance
        """
        # TODO: Add validation
        return self._obj
