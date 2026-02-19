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

    inner_port_instance_ref: Optional[ARRef]
    outer_port_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DelegationSwConnector."""
        super().__init__()
        self.inner_port_instance_ref: Optional[ARRef] = None
        self.outer_port_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DelegationSwConnector":
        """Deserialize XML element to DelegationSwConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DelegationSwConnector object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse inner_port_instance_ref
        child = ARObject._find_child_element(element, "INNER-PORT-INSTANCE-REF")
        if child is not None:
            inner_port_instance_ref_value = ARObject._deserialize_by_tag(child, "PortPrototype")
            obj.inner_port_instance_ref = inner_port_instance_ref_value

        # Parse outer_port_ref
        child = ARObject._find_child_element(element, "OUTER-PORT")
        if child is not None:
            outer_port_ref_value = ARObject._deserialize_by_tag(child, "PortPrototype")
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
