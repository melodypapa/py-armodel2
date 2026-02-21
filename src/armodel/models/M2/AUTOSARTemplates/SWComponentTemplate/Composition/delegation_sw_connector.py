"""DelegationSwConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 80)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2016)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_connector import (
    SwConnector,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs.port_in_composition_type_instance_ref import (
    PortInCompositionTypeInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)


class DelegationSwConnector(SwConnector):
    """AUTOSAR DelegationSwConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    inner_port_iref: Optional[PortInCompositionTypeInstanceRef]
    outer_port_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DelegationSwConnector."""
        super().__init__()
        self.inner_port_iref: Optional[PortInCompositionTypeInstanceRef] = None
        self.outer_port_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DelegationSwConnector to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DelegationSwConnector, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize inner_port_iref (instance reference with wrapper "INNER-PORT-IREF")
        if self.inner_port_iref is not None:
            serialized = ARObject._serialize_item(self.inner_port_iref, "PortInCompositionTypeInstanceRef")
            if serialized is not None:
                # Wrap in IREF wrapper element
                iref_wrapper = ET.Element("INNER-PORT-IREF")
                # Append the serialized element as a child (don't flatten it)
                iref_wrapper.append(serialized)
                elem.append(iref_wrapper)

        # Serialize outer_port_ref
        if self.outer_port_ref is not None:
            serialized = ARObject._serialize_item(self.outer_port_ref, "PortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OUTER-PORT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DelegationSwConnector":
        """Deserialize XML element to DelegationSwConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DelegationSwConnector object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DelegationSwConnector, cls).deserialize(element)

        # Parse inner_port_iref (instance reference from wrapper "INNER-PORT-IREF")
        wrapper = ARObject._find_child_element(element, "INNER-PORT-IREF")
        if wrapper is not None:
            # Get the first child element (the actual reference)
            children = list(wrapper)
            if children:
                inner_elem = children[0]
                inner_port_iref_value = ARObject._deserialize_by_tag(inner_elem)
                obj.inner_port_iref = inner_port_iref_value

        # Parse outer_port_ref
        child = ARObject._find_child_element(element, "OUTER-PORT-REF")
        if child is not None:
            outer_port_ref_value = ARRef.deserialize(child)
            obj.outer_port_ref = outer_port_ref_value

        return obj



class DelegationSwConnectorBuilder:
    """Builder for DelegationSwConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DelegationSwConnector = DelegationSwConnector()

    def build(self) -> DelegationSwConnector:
        """Build and return DelegationSwConnector object.

        Returns:
            DelegationSwConnector instance
        """
        # TODO: Add validation
        return self._obj
