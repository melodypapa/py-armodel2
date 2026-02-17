"""ValueGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 458)

JSON Source: docs/json/packages/M2_MSR_CalibrationData_CalibrationValue.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multilanguage_long_name import (
    MultilanguageLongName,
)
from armodel.models.M2.MSR.CalibrationData.CalibrationValue.sw_values import (
    SwValues,
)


class ValueGroup(ARObject):
    """AUTOSAR ValueGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "label": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultilanguageLongName,
        ),  # label
        "vg_contents": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwValues,
        ),  # vgContents
    }

    def __init__(self) -> None:
        """Initialize ValueGroup."""
        super().__init__()
        self.label: Optional[MultilanguageLongName] = None
        self.vg_contents: Optional[SwValues] = None


class ValueGroupBuilder:
    """Builder for ValueGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ValueGroup = ValueGroup()

    def build(self) -> ValueGroup:
        """Build and return ValueGroup object.

        Returns:
            ValueGroup instance
        """
        # TODO: Add validation
        return self._obj
