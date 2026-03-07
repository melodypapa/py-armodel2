"""DiagnosticComControlSubNodeChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 110)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_CommunicationControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticComControlSubNodeChannel(ARObject):
    """AUTOSAR DiagnosticComControlSubNodeChannel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-COM-CONTROL-SUB-NODE-CHANNEL"


    sub_node_ref: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "SUB-NODE-REF": lambda obj, elem: setattr(obj, "sub_node_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticComControlSubNodeChannel."""
        super().__init__()
        self.sub_node_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticComControlSubNodeChannel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticComControlSubNodeChannel, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sub_node_ref
        if self.sub_node_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sub_node_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUB-NODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticComControlSubNodeChannel":
        """Deserialize XML element to DiagnosticComControlSubNodeChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticComControlSubNodeChannel object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticComControlSubNodeChannel, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SUB-NODE-REF":
                setattr(obj, "sub_node_ref", ARRef.deserialize(child))

        return obj



class DiagnosticComControlSubNodeChannelBuilder(BuilderBase):
    """Builder for DiagnosticComControlSubNodeChannel with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticComControlSubNodeChannel = DiagnosticComControlSubNodeChannel()


    def with_sub_node(self, value: Optional[Any]) -> "DiagnosticComControlSubNodeChannelBuilder":
        """Set sub_node attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sub_node' is required and cannot be None")
        self._obj.sub_node = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "subNode",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticComControlSubNodeChannel:
        """Build and return the DiagnosticComControlSubNodeChannel instance with validation."""
        self._validate_instance()
        return self._obj