"""RPortInCompositionInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 952)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 459)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs.port_in_composition_type_instance_ref import (
    PortInCompositionTypeInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)


class RPortInCompositionInstanceRef(PortInCompositionTypeInstanceRef):
    """AUTOSAR RPortInCompositionInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context_ref: Optional[Any]
    target_r_port_prototype_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize RPortInCompositionInstanceRef."""
        super().__init__()
        self.context_ref: Optional[Any] = None
        self.target_r_port_prototype_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize RPortInCompositionInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RPortInCompositionInstanceRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize context_ref
        if self.context_ref is not None:
            serialized = ARObject._serialize_item(self.context_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_r_port_prototype_ref
        if self.target_r_port_prototype_ref is not None:
            serialized = ARObject._serialize_item(self.target_r_port_prototype_ref, "AbstractRequiredPortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-R-PORT-PROTOTYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RPortInCompositionInstanceRef":
        """Deserialize XML element to RPortInCompositionInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RPortInCompositionInstanceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RPortInCompositionInstanceRef, cls).deserialize(element)

        # Parse context_ref
        child = ARObject._find_child_element(element, "CONTEXT-REF")
        if child is not None:
            context_ref_value = ARRef.deserialize(child)
            obj.context_ref = context_ref_value

        # Parse target_r_port_prototype_ref
        child = ARObject._find_child_element(element, "TARGET-R-PORT-PROTOTYPE-REF")
        if child is not None:
            target_r_port_prototype_ref_value = ARRef.deserialize(child)
            obj.target_r_port_prototype_ref = target_r_port_prototype_ref_value

        return obj



class RPortInCompositionInstanceRefBuilder:
    """Builder for RPortInCompositionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RPortInCompositionInstanceRef = RPortInCompositionInstanceRef()

    def build(self) -> RPortInCompositionInstanceRef:
        """Build and return RPortInCompositionInstanceRef object.

        Returns:
            RPortInCompositionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
