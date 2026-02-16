"""AutosarParameterRef AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class AutosarParameterRef(ARObject):
    """AUTOSAR AutosarParameterRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "autosar": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DataPrototype,
        ),  # autosar
        "local_parameter": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DataPrototype,
        ),  # localParameter
    }

    def __init__(self) -> None:
        """Initialize AutosarParameterRef."""
        super().__init__()
        self.autosar: Optional[DataPrototype] = None
        self.local_parameter: Optional[DataPrototype] = None


class AutosarParameterRefBuilder:
    """Builder for AutosarParameterRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AutosarParameterRef = AutosarParameterRef()

    def build(self) -> AutosarParameterRef:
        """Build and return AutosarParameterRef object.

        Returns:
            AutosarParameterRef instance
        """
        # TODO: Add validation
        return self._obj
