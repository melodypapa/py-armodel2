"""DataPrototype AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)


class DataPrototype(Identifiable):
    """AUTOSAR DataPrototype."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("sw_data_def", None, False, False, SwDataDefProps),  # swDataDef
    ]

    def __init__(self) -> None:
        """Initialize DataPrototype."""
        super().__init__()
        self.sw_data_def: Optional[SwDataDefProps] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DataPrototype to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataPrototype":
        """Create DataPrototype from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DataPrototype instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DataPrototype since parent returns ARObject
        return cast("DataPrototype", obj)


class DataPrototypeBuilder:
    """Builder for DataPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototype = DataPrototype()

    def build(self) -> DataPrototype:
        """Build and return DataPrototype object.

        Returns:
            DataPrototype instance
        """
        # TODO: Add validation
        return self._obj
