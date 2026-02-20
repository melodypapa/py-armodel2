"""PModeGroupInAtomicSwcInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 949)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.mode_group_in_atomic_swc_instance_ref import (
    ModeGroupInAtomicSwcInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
    AbstractProvidedPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class PModeGroupInAtomicSwcInstanceRef(ModeGroupInAtomicSwcInstanceRef):
    """AUTOSAR PModeGroupInAtomicSwcInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context_p_port_prototype_ref: Optional[ARRef]
    target_mode_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize PModeGroupInAtomicSwcInstanceRef."""
        super().__init__()
        self.context_p_port_prototype_ref: Optional[ARRef] = None
        self.target_mode_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize PModeGroupInAtomicSwcInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PModeGroupInAtomicSwcInstanceRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize context_p_port_prototype_ref
        if self.context_p_port_prototype_ref is not None:
            serialized = ARObject._serialize_item(self.context_p_port_prototype_ref, "AbstractProvidedPortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-P-PORT-PROTOTYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_mode_ref
        if self.target_mode_ref is not None:
            serialized = ARObject._serialize_item(self.target_mode_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PModeGroupInAtomicSwcInstanceRef":
        """Deserialize XML element to PModeGroupInAtomicSwcInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PModeGroupInAtomicSwcInstanceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PModeGroupInAtomicSwcInstanceRef, cls).deserialize(element)

        # Parse context_p_port_prototype_ref
        child = ARObject._find_child_element(element, "CONTEXT-P-PORT-PROTOTYPE-REF")
        if child is not None:
            context_p_port_prototype_ref_value = ARRef.deserialize(child)
            obj.context_p_port_prototype_ref = context_p_port_prototype_ref_value

        # Parse target_mode_ref
        child = ARObject._find_child_element(element, "TARGET-MODE-REF")
        if child is not None:
            target_mode_ref_value = ARRef.deserialize(child)
            obj.target_mode_ref = target_mode_ref_value

        return obj



class PModeGroupInAtomicSwcInstanceRefBuilder:
    """Builder for PModeGroupInAtomicSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PModeGroupInAtomicSwcInstanceRef = PModeGroupInAtomicSwcInstanceRef()

    def build(self) -> PModeGroupInAtomicSwcInstanceRef:
        """Build and return PModeGroupInAtomicSwcInstanceRef object.

        Returns:
            PModeGroupInAtomicSwcInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
