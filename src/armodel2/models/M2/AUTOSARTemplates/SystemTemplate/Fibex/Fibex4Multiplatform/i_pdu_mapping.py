"""IPduMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 840)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Multiplatform.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.target_i_pdu_ref import (
    TargetIPduRef,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class IPduMapping(ARObject):
    """AUTOSAR IPduMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "I-PDU-MAPPING"


    introduction: Optional[DocumentationBlock]
    pdu_max_length: Optional[PositiveInteger]
    pdur_tp_chunk: Optional[PositiveInteger]
    source_i_pdu_ref: Optional[ARRef]
    target_i_pdu_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "INTRODUCTION": lambda obj, elem: setattr(obj, "introduction", SerializationHelper.deserialize_by_tag(elem, "DocumentationBlock")),
        "PDU-MAX-LENGTH": lambda obj, elem: setattr(obj, "pdu_max_length", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "PDUR-TP-CHUNK": lambda obj, elem: setattr(obj, "pdur_tp_chunk", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SOURCE-I-PDU-REF": lambda obj, elem: setattr(obj, "source_i_pdu_ref", ARRef.deserialize(elem)),
        "TARGET-I-PDU-REF": lambda obj, elem: setattr(obj, "target_i_pdu_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize IPduMapping."""
        super().__init__()
        self.introduction: Optional[DocumentationBlock] = None
        self.pdu_max_length: Optional[PositiveInteger] = None
        self.pdur_tp_chunk: Optional[PositiveInteger] = None
        self.source_i_pdu_ref: Optional[ARRef] = None
        self.target_i_pdu_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize IPduMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IPduMapping, self).serialize()

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

        # Serialize pdu_max_length
        if self.pdu_max_length is not None:
            serialized = SerializationHelper.serialize_item(self.pdu_max_length, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PDU-MAX-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pdur_tp_chunk
        if self.pdur_tp_chunk is not None:
            serialized = SerializationHelper.serialize_item(self.pdur_tp_chunk, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PDUR-TP-CHUNK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize source_i_pdu_ref
        if self.source_i_pdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.source_i_pdu_ref, "PduTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOURCE-I-PDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_i_pdu_ref
        if self.target_i_pdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_i_pdu_ref, "TargetIPduRef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-I-PDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IPduMapping":
        """Deserialize XML element to IPduMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IPduMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IPduMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "INTRODUCTION":
                setattr(obj, "introduction", SerializationHelper.deserialize_by_tag(child, "DocumentationBlock"))
            elif tag == "PDU-MAX-LENGTH":
                setattr(obj, "pdu_max_length", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "PDUR-TP-CHUNK":
                setattr(obj, "pdur_tp_chunk", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SOURCE-I-PDU-REF":
                setattr(obj, "source_i_pdu_ref", ARRef.deserialize(child))
            elif tag == "TARGET-I-PDU-REF":
                setattr(obj, "target_i_pdu_ref", ARRef.deserialize(child))

        return obj



class IPduMappingBuilder(BuilderBase):
    """Builder for IPduMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IPduMapping = IPduMapping()


    def with_introduction(self, value: Optional[DocumentationBlock]) -> "IPduMappingBuilder":
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

    def with_pdu_max_length(self, value: Optional[PositiveInteger]) -> "IPduMappingBuilder":
        """Set pdu_max_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'pdu_max_length' is required and cannot be None")
        self._obj.pdu_max_length = value
        return self

    def with_pdur_tp_chunk(self, value: Optional[PositiveInteger]) -> "IPduMappingBuilder":
        """Set pdur_tp_chunk attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'pdur_tp_chunk' is required and cannot be None")
        self._obj.pdur_tp_chunk = value
        return self

    def with_source_i_pdu(self, value: Optional[PduTriggering]) -> "IPduMappingBuilder":
        """Set source_i_pdu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'source_i_pdu' is required and cannot be None")
        self._obj.source_i_pdu = value
        return self

    def with_target_i_pdu(self, value: Optional[TargetIPduRef]) -> "IPduMappingBuilder":
        """Set target_i_pdu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'target_i_pdu' is required and cannot be None")
        self._obj.target_i_pdu = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "introduction",
        "pduMaxLength",
        "pdurTpChunk",
        "sourceIPdu",
        "targetIPdu",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> IPduMapping:
        """Build and return the IPduMapping instance with validation."""
        self._validate_instance()
        return self._obj