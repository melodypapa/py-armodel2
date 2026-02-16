"""RuleBasedValueCont AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.value_list import (
    ValueList,
)


class RuleBasedValueCont(ARObject):
    """AUTOSAR RuleBasedValueCont."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "rule_based": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (RuleBasedValue),
        ),  # ruleBased
        "sw_arraysize": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ValueList,
        ),  # swArraysize
        "unit": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Unit,
        ),  # unit
    }

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
