"""ApplicationArrayDataType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 252)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1995)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 35)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_Datatypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_composite_data_type import (
    ApplicationCompositeDataType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class ApplicationArrayDataType(ApplicationCompositeDataType):
    """AUTOSAR ApplicationArrayDataType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dynamic_array: Optional[String]
    element: Optional[Any]
    def __init__(self) -> None:
        """Initialize ApplicationArrayDataType."""
        super().__init__()
        self.dynamic_array: Optional[String] = None
        self.element: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationArrayDataType":
        """Deserialize XML element to ApplicationArrayDataType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationArrayDataType object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse dynamic_array
        child = ARObject._find_child_element(element, "DYNAMIC-ARRAY")
        if child is not None:
            dynamic_array_value = child.text
            obj.dynamic_array = dynamic_array_value

        # Parse element
        child = ARObject._find_child_element(element, "ELEMENT")
        if child is not None:
            element_value = child.text
            obj.element = element_value

        return obj



class ApplicationArrayDataTypeBuilder:
    """Builder for ApplicationArrayDataType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationArrayDataType = ApplicationArrayDataType()

    def build(self) -> ApplicationArrayDataType:
        """Build and return ApplicationArrayDataType object.

        Returns:
            ApplicationArrayDataType instance
        """
        # TODO: Add validation
        return self._obj
