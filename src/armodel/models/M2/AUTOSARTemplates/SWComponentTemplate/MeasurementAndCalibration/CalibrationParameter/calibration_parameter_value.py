"""CalibrationParameterValue AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.flat_instance_descriptor import (
    FlatInstanceDescriptor,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)


class CalibrationParameterValue(ARObject):
    """AUTOSAR CalibrationParameterValue."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("appl_init_value", None, False, False, ValueSpecification),  # applInitValue
        ("impl_init_value", None, False, False, ValueSpecification),  # implInitValue
        ("initialized", None, False, False, FlatInstanceDescriptor),  # initialized
    ]

    def __init__(self) -> None:
        """Initialize CalibrationParameterValue."""
        super().__init__()
        self.appl_init_value: Optional[ValueSpecification] = None
        self.impl_init_value: Optional[ValueSpecification] = None
        self.initialized: Optional[FlatInstanceDescriptor] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CalibrationParameterValue to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CalibrationParameterValue":
        """Create CalibrationParameterValue from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CalibrationParameterValue instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CalibrationParameterValue since parent returns ARObject
        return cast("CalibrationParameterValue", obj)


class CalibrationParameterValueBuilder:
    """Builder for CalibrationParameterValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CalibrationParameterValue = CalibrationParameterValue()

    def build(self) -> CalibrationParameterValue:
        """Build and return CalibrationParameterValue object.

        Returns:
            CalibrationParameterValue instance
        """
        # TODO: Add validation
        return self._obj
