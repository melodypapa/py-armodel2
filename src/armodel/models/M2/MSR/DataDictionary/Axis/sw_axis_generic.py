"""SwAxisGeneric AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.DataDictionary.Axis.sw_axis_type import (
    SwAxisType,
)
from armodel.models.M2.MSR.DataDictionary.Axis.sw_generic_axis_param import (
    SwGenericAxisParam,
)


class SwAxisGeneric(ARObject):
    """AUTOSAR SwAxisGeneric."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "sw_axis_type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwAxisType,
        ),  # swAxisType
        "sw_generic_axis_params": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SwGenericAxisParam,
        ),  # swGenericAxisParams
    }

    def __init__(self) -> None:
        """Initialize SwAxisGeneric."""
        super().__init__()
        self.sw_axis_type: Optional[SwAxisType] = None
        self.sw_generic_axis_params: list[SwGenericAxisParam] = []


class SwAxisGenericBuilder:
    """Builder for SwAxisGeneric."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwAxisGeneric = SwAxisGeneric()

    def build(self) -> SwAxisGeneric:
        """Build and return SwAxisGeneric object.

        Returns:
            SwAxisGeneric instance
        """
        # TODO: Add validation
        return self._obj
