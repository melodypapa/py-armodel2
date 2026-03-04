"""GeneralAnnotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 162)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 163)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_GeneralAnnotation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel2.models.M2.MSR.Documentation.TextModel.MultilanguageData.multilanguage_long_name import (
    MultilanguageLongName,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


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
    _DESERIALIZE_DISPATCH = {
        "ANNOTATION": lambda obj, elem: setattr(obj, "annotation", SerializationHelper.deserialize_by_tag(elem, "String")),
        "ANNOTATION-TEXT": lambda obj, elem: setattr(obj, "annotation_text", SerializationHelper.deserialize_by_tag(elem, "DocumentationBlock")),
        "LABEL": lambda obj, elem: setattr(obj, "label", SerializationHelper.deserialize_by_tag(elem, "MultilanguageLongName")),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ANNOTATION":
                setattr(obj, "annotation", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "ANNOTATION-TEXT":
                setattr(obj, "annotation_text", SerializationHelper.deserialize_by_tag(child, "DocumentationBlock"))
            elif tag == "LABEL":
                setattr(obj, "label", SerializationHelper.deserialize_by_tag(child, "MultilanguageLongName"))

        return obj



class GeneralAnnotationBuilder(BuilderBase, ABC):
    """Builder for GeneralAnnotation with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: GeneralAnnotation = GeneralAnnotation()


    def with_annotation(self, value: String) -> "GeneralAnnotationBuilder":
        """Set annotation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.annotation = value
        return self

    def with_annotation_text(self, value: DocumentationBlock) -> "GeneralAnnotationBuilder":
        """Set annotation_text attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.annotation_text = value
        return self

    def with_label(self, value: Optional[MultilanguageLongName]) -> "GeneralAnnotationBuilder":
        """Set label attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.label = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "annotation",
        "annotationText",
    }
    _OPTIONAL_ATTRIBUTES = {
        "label",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Validate required attributes using pre-computed constants (O(1) lookup)
        # This is much faster than calling get_type_hints() at runtime
        if getattr(self._obj, "annotation", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError(f"Required attribute 'annotation' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn(f"Required attribute 'annotation' is None", UserWarning)
        if getattr(self._obj, "annotationText", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError(f"Required attribute 'annotationText' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn(f"Required attribute 'annotationText' is None", UserWarning)


    @abstractmethod
    def build(self) -> GeneralAnnotation:
        """Build and return the GeneralAnnotation instance (abstract)."""
        raise NotImplementedError