"""AutosarDataPrototype AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.autosar_data_type import (
    AutosarDataType,
)


class AutosarDataPrototype(DataPrototype):
    """AUTOSAR AutosarDataPrototype."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AutosarDataType,
        ),  # type
    }

    def __init__(self) -> None:
        """Initialize AutosarDataPrototype."""
        super().__init__()
        self.type: Optional[AutosarDataType] = None


class AutosarDataPrototypeBuilder:
    """Builder for AutosarDataPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AutosarDataPrototype = AutosarDataPrototype()

    def build(self) -> AutosarDataPrototype:
        """Build and return AutosarDataPrototype object.

        Returns:
            AutosarDataPrototype instance
        """
        # TODO: Add validation
        return self._obj
