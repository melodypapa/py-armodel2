"""EngineeringObject AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 132)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 160)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_EngineeringObject.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    RevisionLabelString,
)
from abc import ABC, abstractmethod


class EngineeringObject(ARObject, ABC):
    """AUTOSAR EngineeringObject."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    category: NameToken
    domain: Optional[NameToken]
    revision_label_strings: list[RevisionLabelString]
    short_label: NameToken
    def __init__(self) -> None:
        """Initialize EngineeringObject."""
        super().__init__()
        self.category: NameToken = None
        self.domain: Optional[NameToken] = None
        self.revision_label_strings: list[RevisionLabelString] = []
        self.short_label: NameToken = None

    def serialize(self) -> ET.Element:
        """Serialize EngineeringObject to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize category
        if self.category is not None:
            serialized = ARObject._serialize_item(self.category, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CATEGORY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize domain
        if self.domain is not None:
            serialized = ARObject._serialize_item(self.domain, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DOMAIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize revision_label_strings (list to container "REVISION-LABEL-STRINGS")
        if self.revision_label_strings:
            wrapper = ET.Element("REVISION-LABEL-STRINGS")
            for item in self.revision_label_strings:
                serialized = ARObject._serialize_item(item, "RevisionLabelString")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize short_label
        if self.short_label is not None:
            serialized = ARObject._serialize_item(self.short_label, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHORT-LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EngineeringObject":
        """Deserialize XML element to EngineeringObject object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EngineeringObject object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse category
        child = ARObject._find_child_element(element, "CATEGORY")
        if child is not None:
            category_value = child.text
            obj.category = category_value

        # Parse domain
        child = ARObject._find_child_element(element, "DOMAIN")
        if child is not None:
            domain_value = child.text
            obj.domain = domain_value

        # Parse revision_label_strings (list from container "REVISION-LABEL-STRINGS")
        obj.revision_label_strings = []
        container = ARObject._find_child_element(element, "REVISION-LABEL-STRINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.revision_label_strings.append(child_value)

        # Parse short_label
        child = ARObject._find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = child.text
            obj.short_label = short_label_value

        return obj



class EngineeringObjectBuilder:
    """Builder for EngineeringObject."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EngineeringObject = EngineeringObject()

    def build(self) -> EngineeringObject:
        """Build and return EngineeringObject object.

        Returns:
            EngineeringObject instance
        """
        # TODO: Add validation
        return self._obj
