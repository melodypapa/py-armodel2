"""AssemblySwConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 289)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 80)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2000)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 423)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_connector import (
    SwConnector,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs.p_port_in_composition_instance_ref import (
    PPortInCompositionInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs.r_port_in_composition_instance_ref import (
    RPortInCompositionInstanceRef,
)


class AssemblySwConnector(SwConnector):
    """AUTOSAR AssemblySwConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    provider_iref: Optional[PPortInCompositionInstanceRef]
    requester_iref: Optional[RPortInCompositionInstanceRef]
    def __init__(self) -> None:
        """Initialize AssemblySwConnector."""
        super().__init__()
        self.provider_iref: Optional[PPortInCompositionInstanceRef] = None
        self.requester_iref: Optional[RPortInCompositionInstanceRef] = None

    def serialize(self) -> ET.Element:
        """Serialize AssemblySwConnector to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AssemblySwConnector, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize provider_iref (instance reference with wrapper "PROVIDER-IREF")
        if self.provider_iref is not None:
            serialized = ARObject._serialize_item(self.provider_iref, "PPortInCompositionInstanceRef")
            if serialized is not None:
                # Wrap in IREF wrapper element
                iref_wrapper = ET.Element("PROVIDER-IREF")
                # Flatten: append children of serialized element directly to iref wrapper
                for child in serialized:
                    iref_wrapper.append(child)
                elem.append(iref_wrapper)

        # Serialize requester_iref (instance reference with wrapper "REQUESTER-IREF")
        if self.requester_iref is not None:
            serialized = ARObject._serialize_item(self.requester_iref, "RPortInCompositionInstanceRef")
            if serialized is not None:
                # Wrap in IREF wrapper element
                iref_wrapper = ET.Element("REQUESTER-IREF")
                # Flatten: append children of serialized element directly to iref wrapper
                for child in serialized:
                    iref_wrapper.append(child)
                elem.append(iref_wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AssemblySwConnector":
        """Deserialize XML element to AssemblySwConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AssemblySwConnector object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AssemblySwConnector, cls).deserialize(element)

        # Parse provider_iref (instance reference from wrapper "PROVIDER-IREF")
        wrapper = ARObject._find_child_element(element, "PROVIDER-IREF")
        if wrapper is not None:
            # Deserialize wrapper element directly as the type (flattened structure)
            provider_iref_value = ARObject._deserialize_by_tag(wrapper, "PPortInCompositionInstanceRef")
            obj.provider_iref = provider_iref_value

        # Parse requester_iref (instance reference from wrapper "REQUESTER-IREF")
        wrapper = ARObject._find_child_element(element, "REQUESTER-IREF")
        if wrapper is not None:
            # Deserialize wrapper element directly as the type (flattened structure)
            requester_iref_value = ARObject._deserialize_by_tag(wrapper, "RPortInCompositionInstanceRef")
            obj.requester_iref = requester_iref_value

        return obj



class AssemblySwConnectorBuilder:
    """Builder for AssemblySwConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AssemblySwConnector = AssemblySwConnector()

    def build(self) -> AssemblySwConnector:
        """Build and return AssemblySwConnector object.

        Returns:
            AssemblySwConnector instance
        """
        # TODO: Add validation
        return self._obj
