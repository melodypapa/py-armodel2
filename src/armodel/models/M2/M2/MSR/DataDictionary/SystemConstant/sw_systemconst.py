"""SwSystemconst AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)


class SwSystemconst(ARElement):
    """AUTOSAR SwSystemconst."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "sw_data_def": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwDataDefProps,
        ),  # swDataDef
    }

    def __init__(self) -> None:
        """Initialize SwSystemconst."""
        super().__init__()
        self.sw_data_def: Optional[SwDataDefProps] = None


class SwSystemconstBuilder:
    """Builder for SwSystemconst."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwSystemconst = SwSystemconst()

    def build(self) -> SwSystemconst:
        """Build and return SwSystemconst object.

        Returns:
            SwSystemconst instance
        """
        # TODO: Add validation
        return self._obj
