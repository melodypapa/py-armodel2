"""DataComProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 903)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_communication_resource_props import (
    CpSoftwareClusterCommunicationResourceProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster import (
    DataConsistencyPolicyEnum,
    SendIndicationEnum,
)


class DataComProps(CpSoftwareClusterCommunicationResourceProps):
    """AUTOSAR DataComProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data: Optional[DataConsistencyPolicyEnum]
    send_indication_enum: Optional[SendIndicationEnum]
    def __init__(self) -> None:
        """Initialize DataComProps."""
        super().__init__()
        self.data: Optional[DataConsistencyPolicyEnum] = None
        self.send_indication_enum: Optional[SendIndicationEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataComProps":
        """Deserialize XML element to DataComProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataComProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataComProps, cls).deserialize(element)

        # Parse data
        child = ARObject._find_child_element(element, "DATA")
        if child is not None:
            data_value = DataConsistencyPolicyEnum.deserialize(child)
            obj.data = data_value

        # Parse send_indication_enum
        child = ARObject._find_child_element(element, "SEND-INDICATION-ENUM")
        if child is not None:
            send_indication_enum_value = SendIndicationEnum.deserialize(child)
            obj.send_indication_enum = send_indication_enum_value

        return obj



class DataComPropsBuilder:
    """Builder for DataComProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataComProps = DataComProps()

    def build(self) -> DataComProps:
        """Build and return DataComProps object.

        Returns:
            DataComProps instance
        """
        # TODO: Add validation
        return self._obj
