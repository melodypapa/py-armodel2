"""IPduMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 840)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Multiplatform.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.target_i_pdu_ref import (
    TargetIPduRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class IPduMapping(ARObject):
    """AUTOSAR IPduMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    introduction: Optional[DocumentationBlock]
    pdu_max_length: Optional[PositiveInteger]
    pdur_tp_chunk: Optional[PositiveInteger]
    source_i_pdu_ref: Optional[ARRef]
    target_i_pdu_ref: Optional[ARRef]
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
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Parse introduction
        child = SerializationHelper.find_child_element(element, "INTRODUCTION")
        if child is not None:
            introduction_value = SerializationHelper.deserialize_by_tag(child, "DocumentationBlock")
            obj.introduction = introduction_value

        # Parse pdu_max_length
        child = SerializationHelper.find_child_element(element, "PDU-MAX-LENGTH")
        if child is not None:
            pdu_max_length_value = child.text
            obj.pdu_max_length = pdu_max_length_value

        # Parse pdur_tp_chunk
        child = SerializationHelper.find_child_element(element, "PDUR-TP-CHUNK")
        if child is not None:
            pdur_tp_chunk_value = child.text
            obj.pdur_tp_chunk = pdur_tp_chunk_value

        # Parse source_i_pdu_ref
        child = SerializationHelper.find_child_element(element, "SOURCE-I-PDU-REF")
        if child is not None:
            source_i_pdu_ref_value = ARRef.deserialize(child)
            obj.source_i_pdu_ref = source_i_pdu_ref_value

        # Parse target_i_pdu_ref
        child = SerializationHelper.find_child_element(element, "TARGET-I-PDU-REF")
        if child is not None:
            target_i_pdu_ref_value = ARRef.deserialize(child)
            obj.target_i_pdu_ref = target_i_pdu_ref_value

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
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
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
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
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
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
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
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
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
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.target_i_pdu = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> IPduMapping:
        """Build and return the IPduMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj