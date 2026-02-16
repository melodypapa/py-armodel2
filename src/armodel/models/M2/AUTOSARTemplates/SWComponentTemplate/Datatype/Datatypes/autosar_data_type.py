"""AutosarDataType AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)


class AutosarDataType(ARElement):
    """AUTOSAR AutosarDataType."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("sw_data_def", None, False, False, SwDataDefProps),  # swDataDef
    ]

    def __init__(self) -> None:
        """Initialize AutosarDataType."""
        super().__init__()
        self.sw_data_def: Optional[SwDataDefProps] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AutosarDataType to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AutosarDataType":
        """Create AutosarDataType from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AutosarDataType instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AutosarDataType since parent returns ARObject
        return cast("AutosarDataType", obj)


class AutosarDataTypeBuilder:
    """Builder for AutosarDataType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AutosarDataType = AutosarDataType()

    def build(self) -> AutosarDataType:
        """Build and return AutosarDataType object.

        Returns:
            AutosarDataType instance
        """
        # TODO: Add validation
        return self._obj
