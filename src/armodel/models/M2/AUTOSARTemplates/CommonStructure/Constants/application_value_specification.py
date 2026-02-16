"""ApplicationValueSpecification AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.MSR.CalibrationData.CalibrationValue.sw_axis_cont import (
    SwAxisCont,
)
from armodel.models.M2.MSR.CalibrationData.CalibrationValue.sw_value_cont import (
    SwValueCont,
)


class ApplicationValueSpecification(ValueSpecification):
    """AUTOSAR ApplicationValueSpecification."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("category", None, True, False, None),  # category
        ("sw_axis_conts", None, False, True, SwAxisCont),  # swAxisConts
        ("sw_value_cont", None, False, False, SwValueCont),  # swValueCont
    ]

    def __init__(self) -> None:
        """Initialize ApplicationValueSpecification."""
        super().__init__()
        self.category: Optional[Identifier] = None
        self.sw_axis_conts: list[SwAxisCont] = []
        self.sw_value_cont: Optional[SwValueCont] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ApplicationValueSpecification to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationValueSpecification":
        """Create ApplicationValueSpecification from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ApplicationValueSpecification instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ApplicationValueSpecification since parent returns ARObject
        return cast("ApplicationValueSpecification", obj)


class ApplicationValueSpecificationBuilder:
    """Builder for ApplicationValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationValueSpecification = ApplicationValueSpecification()

    def build(self) -> ApplicationValueSpecification:
        """Build and return ApplicationValueSpecification object.

        Returns:
            ApplicationValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
