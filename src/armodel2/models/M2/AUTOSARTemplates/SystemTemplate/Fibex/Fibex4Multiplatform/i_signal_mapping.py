"""ISignalMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 846)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Multiplatform.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_triggering import (
    ISignalTriggering,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ISignalMapping(ARObject):
    """AUTOSAR ISignalMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "I-SIGNAL-MAPPING"


    introduction: Optional[DocumentationBlock]
    source_signal_ref: Optional[ARRef]
    target_signal_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "INTRODUCTION": lambda obj, elem: setattr(obj, "introduction", SerializationHelper.deserialize_by_tag(elem, "DocumentationBlock")),
        "SOURCE-SIGNAL-REF": lambda obj, elem: setattr(obj, "source_signal_ref", ARRef.deserialize(elem)),
        "TARGET-SIGNAL-REF": lambda obj, elem: setattr(obj, "target_signal_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize ISignalMapping."""
        super().__init__()
        self.introduction: Optional[DocumentationBlock] = None
        self.source_signal_ref: Optional[ARRef] = None
        self.target_signal_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ISignalMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ISignalMapping, self).serialize()

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

        # Serialize source_signal_ref
        if self.source_signal_ref is not None:
            serialized = SerializationHelper.serialize_item(self.source_signal_ref, "ISignalTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOURCE-SIGNAL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_signal_ref
        if self.target_signal_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_signal_ref, "ISignalTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-SIGNAL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ISignalMapping":
        """Deserialize XML element to ISignalMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ISignalMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ISignalMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "INTRODUCTION":
                setattr(obj, "introduction", SerializationHelper.deserialize_by_tag(child, "DocumentationBlock"))
            elif tag == "SOURCE-SIGNAL-REF":
                setattr(obj, "source_signal_ref", ARRef.deserialize(child))
            elif tag == "TARGET-SIGNAL-REF":
                setattr(obj, "target_signal_ref", ARRef.deserialize(child))

        return obj



class ISignalMappingBuilder(BuilderBase):
    """Builder for ISignalMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ISignalMapping = ISignalMapping()


    def with_introduction(self, value: Optional[DocumentationBlock]) -> "ISignalMappingBuilder":
        """Set introduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'introduction' is required and cannot be None")
        self._obj.introduction = value
        return self

    def with_source_signal(self, value: Optional[ISignalTriggering]) -> "ISignalMappingBuilder":
        """Set source_signal attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'source_signal' is required and cannot be None")
        self._obj.source_signal = value
        return self

    def with_target_signal(self, value: Optional[ISignalTriggering]) -> "ISignalMappingBuilder":
        """Set target_signal attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'target_signal' is required and cannot be None")
        self._obj.target_signal = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "introduction",
        "sourceSignal",
        "targetSignal",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ISignalMapping:
        """Build and return the ISignalMapping instance with validation."""
        self._validate_instance()
        return self._obj