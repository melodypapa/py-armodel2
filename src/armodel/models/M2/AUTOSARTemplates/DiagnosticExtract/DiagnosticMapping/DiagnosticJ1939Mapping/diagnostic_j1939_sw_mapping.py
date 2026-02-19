"""DiagnosticJ1939SwMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 268)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_DiagnosticJ1939Mapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.J1939.diagnostic_j1939_node import (
    DiagnosticJ1939Node,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_component_prototype import (
    SwComponentPrototype,
)


class DiagnosticJ1939SwMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticJ1939SwMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    node: Optional[DiagnosticJ1939Node]
    sw_component_prototype_composition_instance_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DiagnosticJ1939SwMapping."""
        super().__init__()
        self.node: Optional[DiagnosticJ1939Node] = None
        self.sw_component_prototype_composition_instance_ref: Optional[ARRef] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticJ1939SwMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticJ1939SwMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize node
        if self.node is not None:
            serialized = ARObject._serialize_item(self.node, "DiagnosticJ1939Node")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_component_prototype_composition_instance_ref
        if self.sw_component_prototype_composition_instance_ref is not None:
            serialized = ARObject._serialize_item(self.sw_component_prototype_composition_instance_ref, "SwComponentPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-COMPONENT-PROTOTYPE-COMPOSITION-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticJ1939SwMapping":
        """Deserialize XML element to DiagnosticJ1939SwMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticJ1939SwMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticJ1939SwMapping, cls).deserialize(element)

        # Parse node
        child = ARObject._find_child_element(element, "NODE")
        if child is not None:
            node_value = ARObject._deserialize_by_tag(child, "DiagnosticJ1939Node")
            obj.node = node_value

        # Parse sw_component_prototype_composition_instance_ref
        child = ARObject._find_child_element(element, "SW-COMPONENT-PROTOTYPE-COMPOSITION-INSTANCE-REF")
        if child is not None:
            sw_component_prototype_composition_instance_ref_value = ARObject._deserialize_by_tag(child, "SwComponentPrototype")
            obj.sw_component_prototype_composition_instance_ref = sw_component_prototype_composition_instance_ref_value

        return obj



class DiagnosticJ1939SwMappingBuilder:
    """Builder for DiagnosticJ1939SwMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticJ1939SwMapping = DiagnosticJ1939SwMapping()

    def build(self) -> DiagnosticJ1939SwMapping:
        """Build and return DiagnosticJ1939SwMapping object.

        Returns:
            DiagnosticJ1939SwMapping instance
        """
        # TODO: Add validation
        return self._obj
