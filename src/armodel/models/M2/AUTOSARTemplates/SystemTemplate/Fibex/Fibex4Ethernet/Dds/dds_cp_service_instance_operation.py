"""DdsCpServiceInstanceOperation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 475)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class DdsCpServiceInstanceOperation(ARObject):
    """AUTOSAR DdsCpServiceInstanceOperation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dds_operation_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DdsCpServiceInstanceOperation."""
        super().__init__()
        self.dds_operation_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsCpServiceInstanceOperation":
        """Deserialize XML element to DdsCpServiceInstanceOperation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsCpServiceInstanceOperation object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse dds_operation_ref
        child = ARObject._find_child_element(element, "DDS-OPERATION")
        if child is not None:
            dds_operation_ref_value = ARObject._deserialize_by_tag(child, "PduTriggering")
            obj.dds_operation_ref = dds_operation_ref_value

        return obj



class DdsCpServiceInstanceOperationBuilder:
    """Builder for DdsCpServiceInstanceOperation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsCpServiceInstanceOperation = DdsCpServiceInstanceOperation()

    def build(self) -> DdsCpServiceInstanceOperation:
        """Build and return DdsCpServiceInstanceOperation object.

        Returns:
            DdsCpServiceInstanceOperation instance
        """
        # TODO: Add validation
        return self._obj
