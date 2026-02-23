"""GeneralAnnotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 162)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 163)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_GeneralAnnotation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multilanguage_long_name import (
    MultilanguageLongName,
)
from abc import ABC, abstractmethod


class GeneralAnnotation(ARObject, ABC):
    """AUTOSAR GeneralAnnotation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    annotation: String
    annotation_text: DocumentationBlock
    label: Optional[MultilanguageLongName]
    def __init__(self) -> None:
        """Initialize GeneralAnnotation."""
        super().__init__()
        self.annotation: String = None
        self.annotation_text: DocumentationBlock = None
        self.label: Optional[MultilanguageLongName] = None

    def serialize(self) -> ET.Element:
        """Serialize GeneralAnnotation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(GeneralAnnotation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize annotation
        if self.annotation is not None:
            serialized = SerializationHelper.serialize_item(self.annotation, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ANNOTATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize annotation_text
        if self.annotation_text is not None:
            serialized = SerializationHelper.serialize_item(self.annotation_text, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ANNOTATION-TEXT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize label
        if self.label is not None:
            serialized = SerializationHelper.serialize_item(self.label, "MultilanguageLongName")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GeneralAnnotation":
        """Deserialize XML element to GeneralAnnotation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GeneralAnnotation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(GeneralAnnotation, cls).deserialize(element)

        # Parse annotation
        child = SerializationHelper.find_child_element(element, "ANNOTATION")
        if child is not None:
            annotation_value = child.text
            obj.annotation = annotation_value

        # Parse annotation_text
        child = SerializationHelper.find_child_element(element, "ANNOTATION-TEXT")
        if child is not None:
            annotation_text_value = SerializationHelper.deserialize_by_tag(child, "DocumentationBlock")
            obj.annotation_text = annotation_text_value

        # Parse label
        child = SerializationHelper.find_child_element(element, "LABEL")
        if child is not None:
            label_value = SerializationHelper.deserialize_by_tag(child, "MultilanguageLongName")
            obj.label = label_value

        return obj



