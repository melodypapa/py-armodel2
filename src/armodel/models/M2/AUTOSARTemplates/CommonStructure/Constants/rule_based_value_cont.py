"""RuleBasedValueCont AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 330)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 464)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.value_list import (
    ValueList,
)


class RuleBasedValueCont(ARObject):
    """AUTOSAR RuleBasedValueCont."""

    rule_based: Optional[Any]
    sw_arraysize: Optional[ValueList]
    unit: Optional[Unit]
    def __init__(self) -> None:
        """Initialize RuleBasedValueCont."""
        super().__init__()
        self.rule_based: Optional[Any] = None
        self.sw_arraysize: Optional[ValueList] = None
        self.unit: Optional[Unit] = None


class RuleBasedValueContBuilder:
    """Builder for RuleBasedValueCont."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RuleBasedValueCont = RuleBasedValueCont()

    def build(self) -> RuleBasedValueCont:
        """Build and return RuleBasedValueCont object.

        Returns:
            RuleBasedValueCont instance
        """
        # TODO: Add validation
        return self._obj
