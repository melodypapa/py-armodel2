"""DataMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 981)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 217)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from abc import ABC, abstractmethod


class DataMapping(ARObject, ABC):
    """AUTOSAR DataMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    introduction: Optional[DocumentationBlock]
    def __init__(self) -> None:
        """Initialize DataMapping."""
        super().__init__()
        self.introduction: Optional[DocumentationBlock] = None
    def serialize(self) -> ET.Element:
        """Serialize DataMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize introduction
        if self.introduction is not None:
            serialized = ARObject._serialize_item(self.introduction, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INTRODUCTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataMapping":
        """Deserialize XML element to DataMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse introduction
        child = ARObject._find_child_element(element, "INTRODUCTION")
        if child is not None:
            introduction_value = ARObject._deserialize_by_tag(child, "DocumentationBlock")
            obj.introduction = introduction_value

        return obj



class DataMappingBuilder:
    """Builder for DataMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataMapping = DataMapping()

    def build(self) -> DataMapping:
        """Build and return DataMapping object.

        Returns:
            DataMapping instance
        """
        # TODO: Add validation
        return self._obj
