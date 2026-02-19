"""IncludedDataTypeSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 600)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_IncludedDataTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.autosar_data_type import (
    AutosarDataType,
)


class IncludedDataTypeSet(ARObject):
    """AUTOSAR IncludedDataTypeSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_types: list[AutosarDataType]
    literal_prefix: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize IncludedDataTypeSet."""
        super().__init__()
        self.data_types: list[AutosarDataType] = []
        self.literal_prefix: Optional[Identifier] = None
    def serialize(self) -> ET.Element:
        """Serialize IncludedDataTypeSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize data_types (list to container "DATA-TYPES")
        if self.data_types:
            wrapper = ET.Element("DATA-TYPES")
            for item in self.data_types:
                serialized = ARObject._serialize_item(item, "AutosarDataType")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize literal_prefix
        if self.literal_prefix is not None:
            serialized = ARObject._serialize_item(self.literal_prefix, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LITERAL-PREFIX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IncludedDataTypeSet":
        """Deserialize XML element to IncludedDataTypeSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IncludedDataTypeSet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_types (list from container "DATA-TYPES")
        obj.data_types = []
        container = ARObject._find_child_element(element, "DATA-TYPES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_types.append(child_value)

        # Parse literal_prefix
        child = ARObject._find_child_element(element, "LITERAL-PREFIX")
        if child is not None:
            literal_prefix_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.literal_prefix = literal_prefix_value

        return obj



class IncludedDataTypeSetBuilder:
    """Builder for IncludedDataTypeSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IncludedDataTypeSet = IncludedDataTypeSet()

    def build(self) -> IncludedDataTypeSet:
        """Build and return IncludedDataTypeSet object.

        Returns:
            IncludedDataTypeSet instance
        """
        # TODO: Add validation
        return self._obj
