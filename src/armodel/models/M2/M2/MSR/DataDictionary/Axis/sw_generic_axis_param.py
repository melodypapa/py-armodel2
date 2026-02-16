"""SwGenericAxisParam AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.DataDictionary.Axis.sw_generic_axis_param import (
    SwGenericAxisParam,
)


class SwGenericAxisParam(ARObject):
    """AUTOSAR SwGenericAxisParam."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "sw_generic_axis_param": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwGenericAxisParam,
        ),  # swGenericAxisParam
    }

    def __init__(self) -> None:
        """Initialize SwGenericAxisParam."""
        super().__init__()
        self.sw_generic_axis_param: Optional[SwGenericAxisParam] = None


class SwGenericAxisParamBuilder:
    """Builder for SwGenericAxisParam."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwGenericAxisParam = SwGenericAxisParam()

    def build(self) -> SwGenericAxisParam:
        """Build and return SwGenericAxisParam object.

        Returns:
            SwGenericAxisParam instance
        """
        # TODO: Add validation
        return self._obj
