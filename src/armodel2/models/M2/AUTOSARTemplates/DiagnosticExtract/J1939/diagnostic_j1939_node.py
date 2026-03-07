"""DiagnosticJ1939Node AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 267)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_J1939.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import DiagnosticCommonElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.j1939_nm_node import (
    J1939NmNode,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticJ1939Node(DiagnosticCommonElement):
    """AUTOSAR DiagnosticJ1939Node."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-J1939-NODE"


    nm_node_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "NM-NODE-REF": lambda obj, elem: setattr(obj, "nm_node_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticJ1939Node."""
        super().__init__()
        self.nm_node_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticJ1939Node to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticJ1939Node, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize nm_node_ref
        if self.nm_node_ref is not None:
            serialized = SerializationHelper.serialize_item(self.nm_node_ref, "J1939NmNode")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-NODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticJ1939Node":
        """Deserialize XML element to DiagnosticJ1939Node object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticJ1939Node object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticJ1939Node, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "NM-NODE-REF":
                setattr(obj, "nm_node_ref", ARRef.deserialize(child))

        return obj



class DiagnosticJ1939NodeBuilder(DiagnosticCommonElementBuilder):
    """Builder for DiagnosticJ1939Node with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticJ1939Node = DiagnosticJ1939Node()


    def with_nm_node(self, value: Optional[J1939NmNode]) -> "DiagnosticJ1939NodeBuilder":
        """Set nm_node attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'nm_node' is required and cannot be None")
        self._obj.nm_node = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "nmNode",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticJ1939Node:
        """Build and return the DiagnosticJ1939Node instance with validation."""
        self._validate_instance()
        return self._obj