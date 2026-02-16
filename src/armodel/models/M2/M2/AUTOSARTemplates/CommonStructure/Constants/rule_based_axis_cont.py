"""RuleBasedAxisCont AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AxisIndexType,
)
from armodel.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.value_list import (
    ValueList,
)


class RuleBasedAxisCont(ARObject):
    """AUTOSAR RuleBasedAxisCont."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "category": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CalprmAxisCategoryEnum,
        ),  # category
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
        "sw_axis_index": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # swAxisIndex
        "unit": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Unit,
        ),  # unit
    }

    def __init__(self) -> None:
        """Initialize RuleBasedAxisCont."""
        super().__init__()
        self.category: Optional[CalprmAxisCategoryEnum] = None
        self.rule_based: Optional[Any] = None
        self.sw_arraysize: Optional[ValueList] = None
        self.sw_axis_index: Optional[AxisIndexType] = None
        self.unit: Optional[Unit] = None


class RuleBasedAxisContBuilder:
    """Builder for RuleBasedAxisCont."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RuleBasedAxisCont = RuleBasedAxisCont()

    def build(self) -> RuleBasedAxisCont:
        """Build and return RuleBasedAxisCont object.

        Returns:
            RuleBasedAxisCont instance
        """
        # TODO: Add validation
        return self._obj
