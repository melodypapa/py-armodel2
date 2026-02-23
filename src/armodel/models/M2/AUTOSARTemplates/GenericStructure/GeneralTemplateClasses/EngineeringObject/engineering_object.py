"""EngineeringObject AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 132)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 160)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_EngineeringObject.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
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

    short_label: NameToken
    category: NameToken
    domain: Optional[NameToken]
    revision_labels: list[RevisionLabelString]
    def __init__(self) -> None:
        """Initialize EngineeringObject."""
        super().__init__()
        self.short_label: NameToken = None
        self.category: NameToken = None
        self.domain: Optional[NameToken] = None
        self.revision_labels: list[RevisionLabelString] = []

    def serialize(self) -> ET.Element:
        """Serialize EngineeringObject to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EngineeringObject, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize short_label
        if self.short_label is not None:
            serialized = SerializationHelper.serialize_item(self.short_label, "NameToken")
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

        # Serialize category
        if self.category is not None:
            serialized = SerializationHelper.serialize_item(self.category, "NameToken")
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
            serialized = SerializationHelper.serialize_item(self.domain, "NameToken")
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

        # Serialize revision_labels (list to container "REVISION-LABELS")
        if self.revision_labels:
            wrapper = ET.Element("REVISION-LABELS")
            for item in self.revision_labels:
                serialized = SerializationHelper.serialize_item(item, "RevisionLabelString")
                if serialized is not None:
                    child_elem = ET.Element("REVISION-LABEL")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EngineeringObject":
        """Deserialize XML element to EngineeringObject object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EngineeringObject object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EngineeringObject, cls).deserialize(element)

        # Parse short_label
        child = SerializationHelper.find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = child.text
            obj.short_label = short_label_value

        # Parse category
        child = SerializationHelper.find_child_element(element, "CATEGORY")
        if child is not None:
            category_value = child.text
            obj.category = category_value

        # Parse domain
        child = SerializationHelper.find_child_element(element, "DOMAIN")
        if child is not None:
            domain_value = child.text
            obj.domain = domain_value

        # Parse revision_labels (list from container "REVISION-LABELS")
        obj.revision_labels = []
        container = SerializationHelper.find_child_element(element, "REVISION-LABELS")
        if container is not None:
            for child in container:
                # Extract primitive value (RevisionLabelString) as text
                child_value = child.text
                if child_value is not None:
                    obj.revision_labels.append(child_value)

        return obj



