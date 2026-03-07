"""TargetIPduRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 841)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Multiplatform.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.pdu_mapping_default_value import (
    PduMappingDefaultValue,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TargetIPduRef(ARObject):
    """AUTOSAR TargetIPduRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TARGET-I-PDU-REF"


    default_value_ref: Optional[ARRef]
    target_i_pdu_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "DEFAULT-VALUE-REF": lambda obj, elem: setattr(obj, "default_value_ref", ARRef.deserialize(elem)),
        "TARGET-I-PDU-REF": lambda obj, elem: setattr(obj, "target_i_pdu_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize TargetIPduRef."""
        super().__init__()
        self.default_value_ref: Optional[ARRef] = None
        self.target_i_pdu_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize TargetIPduRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TargetIPduRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize default_value_ref
        if self.default_value_ref is not None:
            serialized = SerializationHelper.serialize_item(self.default_value_ref, "PduMappingDefaultValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-VALUE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_i_pdu_ref
        if self.target_i_pdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_i_pdu_ref, "PduTriggering")
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
    def deserialize(cls, element: ET.Element) -> "TargetIPduRef":
        """Deserialize XML element to TargetIPduRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TargetIPduRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TargetIPduRef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DEFAULT-VALUE-REF":
                setattr(obj, "default_value_ref", ARRef.deserialize(child))
            elif tag == "TARGET-I-PDU-REF":
                setattr(obj, "target_i_pdu_ref", ARRef.deserialize(child))

        return obj



class TargetIPduRefBuilder(BuilderBase):
    """Builder for TargetIPduRef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TargetIPduRef = TargetIPduRef()


    def with_default_value(self, value: Optional[PduMappingDefaultValue]) -> "TargetIPduRefBuilder":
        """Set default_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'default_value' is required and cannot be None")
        self._obj.default_value = value
        return self

    def with_target_i_pdu(self, value: Optional[PduTriggering]) -> "TargetIPduRefBuilder":
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
        "defaultValue",
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


    def build(self) -> TargetIPduRef:
        """Build and return the TargetIPduRef instance with validation."""
        self._validate_instance()
        return self._obj