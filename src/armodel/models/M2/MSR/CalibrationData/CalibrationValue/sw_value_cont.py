"""SwValueCont AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData.single_language_unit_names import (
    SingleLanguageUnitNames,
)
from armodel.models.M2.MSR.CalibrationData.CalibrationValue.sw_values import (
    SwValues,
)
from armodel.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.value_list import (
    ValueList,
)


class SwValueCont(ARObject):
    """AUTOSAR SwValueCont."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "sw_arraysize": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ValueList,
        ),  # swArraysize
        "sw_values_phys": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwValues,
        ),  # swValuesPhys
        "unit": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Unit,
        ),  # unit
        "unit_display": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SingleLanguageUnitNames,
        ),  # unitDisplay
    }

    def __init__(self) -> None:
        """Initialize SwValueCont."""
        super().__init__()
        self.sw_arraysize: Optional[ValueList] = None
        self.sw_values_phys: Optional[SwValues] = None
        self.unit: Optional[Unit] = None
        self.unit_display: Optional[SingleLanguageUnitNames] = None


class SwValueContBuilder:
    """Builder for SwValueCont."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwValueCont = SwValueCont()

    def build(self) -> SwValueCont:
        """Build and return SwValueCont object.

        Returns:
            SwValueCont instance
        """
        # TODO: Add validation
        return self._obj
