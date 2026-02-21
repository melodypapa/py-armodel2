"""RVariableInAtomicSwcInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 943)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.variable_in_atomic_swc_instance_ref import (
    VariableInAtomicSwcInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class RVariableInAtomicSwcInstanceRef(VariableInAtomicSwcInstanceRef):
    """AUTOSAR RVariableInAtomicSwcInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context_r_port_prototype_ref: Optional[ARRef]
    target_data_element_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize RVariableInAtomicSwcInstanceRef."""
        super().__init__()
        self.context_r_port_prototype_ref: Optional[ARRef] = None
        self.target_data_element_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize RVariableInAtomicSwcInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RVariableInAtomicSwcInstanceRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize context_r_port_prototype_ref
        if self.context_r_port_prototype_ref is not None:
            serialized = ARObject._serialize_item(self.context_r_port_prototype_ref, "AbstractRequiredPortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-R-PORT-PROTOTYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_data_element_ref
        if self.target_data_element_ref is not None:
            serialized = ARObject._serialize_item(self.target_data_element_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-DATA-ELEMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RVariableInAtomicSwcInstanceRef":
        """Deserialize XML element to RVariableInAtomicSwcInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RVariableInAtomicSwcInstanceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RVariableInAtomicSwcInstanceRef, cls).deserialize(element)

        # Parse context_r_port_prototype_ref
        child = ARObject._find_child_element(element, "CONTEXT-R-PORT-PROTOTYPE-REF")
        if child is not None:
            context_r_port_prototype_ref_value = ARRef.deserialize(child)
            obj.context_r_port_prototype_ref = context_r_port_prototype_ref_value

        # Parse target_data_element_ref
        child = ARObject._find_child_element(element, "TARGET-DATA-ELEMENT-REF")
        if child is not None:
            target_data_element_ref_value = ARRef.deserialize(child)
            obj.target_data_element_ref = target_data_element_ref_value

        return obj



class RVariableInAtomicSwcInstanceRefBuilder:
    """Builder for RVariableInAtomicSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RVariableInAtomicSwcInstanceRef = RVariableInAtomicSwcInstanceRef()

    def build(self) -> RVariableInAtomicSwcInstanceRef:
        """Build and return RVariableInAtomicSwcInstanceRef object.

        Returns:
            RVariableInAtomicSwcInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
