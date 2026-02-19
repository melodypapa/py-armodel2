"""FrGlobalTimeDomainProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 878)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_FR.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.abstract_global_time_domain_props import (
    AbstractGlobalTimeDomainProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class FrGlobalTimeDomainProps(AbstractGlobalTimeDomainProps):
    """AUTOSAR FrGlobalTimeDomainProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ofs_data_id_list: PositiveInteger
    sync_data_id_list: PositiveInteger
    def __init__(self) -> None:
        """Initialize FrGlobalTimeDomainProps."""
        super().__init__()
        self.ofs_data_id_list: PositiveInteger = None
        self.sync_data_id_list: PositiveInteger = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FrGlobalTimeDomainProps":
        """Deserialize XML element to FrGlobalTimeDomainProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FrGlobalTimeDomainProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FrGlobalTimeDomainProps, cls).deserialize(element)

        # Parse ofs_data_id_list
        child = ARObject._find_child_element(element, "OFS-DATA-ID-LIST")
        if child is not None:
            ofs_data_id_list_value = child.text
            obj.ofs_data_id_list = ofs_data_id_list_value

        # Parse sync_data_id_list
        child = ARObject._find_child_element(element, "SYNC-DATA-ID-LIST")
        if child is not None:
            sync_data_id_list_value = child.text
            obj.sync_data_id_list = sync_data_id_list_value

        return obj



class FrGlobalTimeDomainPropsBuilder:
    """Builder for FrGlobalTimeDomainProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FrGlobalTimeDomainProps = FrGlobalTimeDomainProps()

    def build(self) -> FrGlobalTimeDomainProps:
        """Build and return FrGlobalTimeDomainProps object.

        Returns:
            FrGlobalTimeDomainProps instance
        """
        # TODO: Add validation
        return self._obj
