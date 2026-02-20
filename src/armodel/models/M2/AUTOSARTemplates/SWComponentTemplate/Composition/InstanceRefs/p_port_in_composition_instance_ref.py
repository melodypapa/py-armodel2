"""PPortInCompositionInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 951)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs.port_in_composition_type_instance_ref import (
    PortInCompositionTypeInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
    AbstractProvidedPortPrototype,
)


class PPortInCompositionInstanceRef(PortInCompositionTypeInstanceRef):
    """AUTOSAR PPortInCompositionInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context: Optional[Any]
    target_p_port_prototype: Optional[AbstractProvidedPortPrototype]
    def __init__(self) -> None:
        """Initialize PPortInCompositionInstanceRef."""
        super().__init__()
        self.context: Optional[Any] = None
        self.target_p_port_prototype: Optional[AbstractProvidedPortPrototype] = None

    def serialize(self) -> ET.Element:
        """Serialize PPortInCompositionInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PPortInCompositionInstanceRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize context
        if self.context is not None:
            serialized = ARObject._serialize_item(self.context, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_p_port_prototype
        if self.target_p_port_prototype is not None:
            serialized = ARObject._serialize_item(self.target_p_port_prototype, "AbstractProvidedPortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-P-PORT-PROTOTYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PPortInCompositionInstanceRef":
        """Deserialize XML element to PPortInCompositionInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PPortInCompositionInstanceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PPortInCompositionInstanceRef, cls).deserialize(element)

        # Parse context
        child = ARObject._find_child_element(element, "CONTEXT")
        if child is not None:
            context_value = child.text
            obj.context = context_value

        # Parse target_p_port_prototype
        child = ARObject._find_child_element(element, "TARGET-P-PORT-PROTOTYPE")
        if child is not None:
            target_p_port_prototype_value = ARObject._deserialize_by_tag(child, "AbstractProvidedPortPrototype")
            obj.target_p_port_prototype = target_p_port_prototype_value

        return obj



class PPortInCompositionInstanceRefBuilder:
    """Builder for PPortInCompositionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PPortInCompositionInstanceRef = PPortInCompositionInstanceRef()

    def build(self) -> PPortInCompositionInstanceRef:
        """Build and return PPortInCompositionInstanceRef object.

        Returns:
            PPortInCompositionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
