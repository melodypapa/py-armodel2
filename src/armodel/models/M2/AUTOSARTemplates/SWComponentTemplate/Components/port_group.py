"""PortGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 203)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2045)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)


class PortGroup(Identifiable):
    """AUTOSAR PortGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    inner_group_refs: list[ARRef]
    outer_port_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize PortGroup."""
        super().__init__()
        self.inner_group_refs: list[ARRef] = []
        self.outer_port_refs: list[ARRef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "PortGroup":
        """Deserialize XML element to PortGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PortGroup object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse inner_group_refs (list)
        obj.inner_group_refs = []
        for child in ARObject._find_all_child_elements(element, "INNER-GROUPS"):
            inner_group_refs_value = ARObject._deserialize_by_tag(child, "PortGroup")
            obj.inner_group_refs.append(inner_group_refs_value)

        # Parse outer_port_refs (list)
        obj.outer_port_refs = []
        for child in ARObject._find_all_child_elements(element, "OUTER-PORTS"):
            outer_port_refs_value = ARObject._deserialize_by_tag(child, "PortPrototype")
            obj.outer_port_refs.append(outer_port_refs_value)

        return obj



class PortGroupBuilder:
    """Builder for PortGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortGroup = PortGroup()

    def build(self) -> PortGroup:
        """Build and return PortGroup object.

        Returns:
            PortGroup instance
        """
        # TODO: Add validation
        return self._obj
