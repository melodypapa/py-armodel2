"""SignalPathConstraint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2057)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SignalPaths.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SignalPathConstraint(ARObject, ABC):
    """AUTOSAR SignalPathConstraint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    introduction: DocumentationBlock
    _DESERIALIZE_DISPATCH = {
        "INTRODUCTION": lambda obj, elem: setattr(obj, "introduction", SerializationHelper.deserialize_by_tag(elem, "DocumentationBlock")),
    }


    def __init__(self) -> None:
        """Initialize SignalPathConstraint."""
        super().__init__()
        self.introduction: DocumentationBlock = None

    def serialize(self) -> ET.Element:
        """Serialize SignalPathConstraint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SignalPathConstraint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize introduction
        if self.introduction is not None:
            serialized = SerializationHelper.serialize_item(self.introduction, "DocumentationBlock")
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
    def deserialize(cls, element: ET.Element) -> "SignalPathConstraint":
        """Deserialize XML element to SignalPathConstraint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SignalPathConstraint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SignalPathConstraint, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "INTRODUCTION":
                setattr(obj, "introduction", SerializationHelper.deserialize_by_tag(child, "DocumentationBlock"))

        return obj



class SignalPathConstraintBuilder(BuilderBase, ABC):
    """Builder for SignalPathConstraint with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SignalPathConstraint = SignalPathConstraint()


    def with_introduction(self, value: DocumentationBlock) -> "SignalPathConstraintBuilder":
        """Set introduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'introduction' is required and cannot be None")
        self._obj.introduction = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "introduction",
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
        if getattr(self._obj, "introduction", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'introduction' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'introduction' is None", UserWarning)


    @abstractmethod
    def build(self) -> SignalPathConstraint:
        """Build and return the SignalPathConstraint instance (abstract)."""
        raise NotImplementedError